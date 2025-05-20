# bot_geocoder
бот-геокодер, который по запросу пользователя присылает ему карту с запрошенным объектом
# 🗺 Бот-геокодер Telegram

Этот Telegram-бот находит географические объекты по названию или адресу и отправляет пользователю карту с меткой и подписью. Реализовано с использованием Yandex Geocoder API и Static Maps API.

## 🔧 Возможности

- Поиск объекта по текстовому запросу
- Отправка карты с меткой в центральной точке найденного объекта
- Подпись под картой
- Обработка ошибок HTTP и случаев, когда ничего не найдено

## 🛠 Технологии

- Python 3.10+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- aiohttp
- Yandex Geocoder API
- Yandex Static Maps API

## 🚀 Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/geocoder-bot.git
cd geocoder-bot
