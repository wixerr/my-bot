from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

BANKS = {
    "Тинькофф": {
        "reward": "1000 рублей",
        "link": "https://tbank.ru/baf/4V9IL7mZNup",
        "instruction": "1. Перейди по ссылке\n2. Оформи карту\n3. Получи 500 руб на счёт+500 от меня\nсвязь: @wizzerqu"
    },
    "Альфа-Банк": {
        "reward": "500 рублей",
        "link": "https://alfa.me/zNkXWE",
        "instruction": "1. Перейди по ссылке\n2. Оформи карту\n3. Получи 500 руб на счёт"
    },
}
