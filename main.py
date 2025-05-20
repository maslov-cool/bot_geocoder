# Импортируем необходимые классы.
# @geocoder_by_coding_lover_bot --> ник в тг
import logging
import aiohttp
from telegram.ext import Application, CommandHandler


# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
BOT_TOKEN = '7656764921:AAGWmbKCMSakZhmr-oifi6nfdySLWmvUb_k'


async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


async def start(update, context):
    await update.message.reply_text("Я бот-геокодер. Ищу объекты на карте.")


# Определяем функцию-обработчик сообщений.
# У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.
async def geocoder(update, context):
    try:
        geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
        response = await get_response(geocoder_uri, params={
            "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
            "format": "json",
            "geocode": update.message.text
        })

        toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        lon_1, lat_1 = [float(i) for i in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
        lon_2, lat_2 = [float(i) for i in toponym['boundedBy']['Envelope']['upperCorner'].split()]
        lon, lat = toponym["Point"]["pos"].split()

        api_key = '341350ef-a110-4b4b-bd5b-451cf362b837'
        delta1 = str(abs(lon_2 - lon_1))
        delta2 = str(abs(lat_2 - lat_1))
        params = {
            "ll": ",".join([str(i) for i in [float(lon), float(lat)]]),
            "spn": ",".join([delta1, delta2]),
            "apikey": api_key,
            'pt': f'{lon},{lat},org'
        }
        static_api_request = (f"http://static-maps.yandex.ru/1.x/?ll={params['ll']}&spn={params['spn']}"
                              f"&apikey={params['apikey']}&pt={params['pt']}&l=map")

        await context.bot.send_photo(
            update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
            # Ссылка на static API, по сути, ссылка на картинку.
            # Телеграму можно передать прямо её, не скачивая предварительно карту.
            static_api_request,
            caption=f"Нашёл: {' '.join(update.message.text.split()[1:])}"
        )
    except Exception as er:
        await update.message.reply_text(f'Ничего не найдено по адресу {' '.join(update.message.text.split()[1:])}')


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчик в приложении.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("geocoder", geocoder))

    # Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()

