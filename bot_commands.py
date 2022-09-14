import bottoken as token
from telegram import Update
from telegram.ext import Updater, CommandHandler, Filters, CallbackContext, MessageHandler
import datetime
import requests

def stop_command(update: Update, context: CallbackContext):
    update.message.reply_text('выключаюсь...')
    print('--------- STOP ----------')
    quit()


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def ping_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'pong')


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Бот готов к работе!')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Можно просто ввести цифры посчитать, либо использовать команды \
\n/start\n/hi\n/help\n/time\n/sum [число 1] [число 2]\n/multiply [число 1] [число 2]\n/ping\n/stop')


def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')


def multiply_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x*y}')


def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот")
    elif(update.message.text == "stop"):
        update.message.reply_text('выключаюсь...')
        print('--------- STOP ----------')
        quit()
    else:
        try:
            update.message.reply_text(eval(update.message.text))
        except:
            update.message.reply_text("Не понятно")


updater = Updater(token.token)
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('ping', ping_command))
updater.dispatcher.add_handler(CommandHandler('multiply', multiply_command))
updater.dispatcher.add_handler(CommandHandler('stop', stop_command))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))

print('--------- START ----------')
updater.start_polling()
updater.idle()