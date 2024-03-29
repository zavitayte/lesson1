# импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# добавляем логирование для нашего бота
import logging

# настраиваем прокси для работы бота
PROXY = {"proxy_url":"socks5://t1.learn.python.ru:1080",
"urllib3_proxy_kwargs":{"username":"learn","password":"python"}}

# комманда для логирования
logging.basicConfig(format="%(asctime)s- %(levelname)s - %(message)s",
                    level=logging.INFO,
                    filename="bot.log"
                    )

# создаем функцию, которая вызывается при нажатии кнопки старт
def greet_user (bot,update):
    text = "нажали старт /start"
    logging.info(text)
    print(text)
    update.message.reply_text(text)

# функция которая будет отвечать пользователю
def talk_to_me (bot,update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

# функция которая соединяется с платформой телеграм , тело бота
def main():
    mybot = Updater ("838847981:AAHbb1R0ajml71CU83AanDujvM1IYj5Gml4", request_kwargs=PROXY)

    logging.info("Бот запускается")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


# вызываем функция, строчка запускает нашего бота

main()