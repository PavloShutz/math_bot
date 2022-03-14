from telegram.ext import Filters, MessageHandler, CommandHandler, Updater
from pathlib import Path

file = Path.cwd() / 'token.txt'
data = open(file, 'r')
info = data.read()
data.close()
TOKEN = info

updater = Updater(TOKEN)


def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Hello! I\'m math bot. Type \help for more info')


def helper(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Type any operation you want, and that\'s all 😁')


def reply_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    try:
        # Я принципиально не буду менять этот способ -- для этого случая он более чем хороший
        result = eval(message)
        text = f"{result}"
        context.bot.send_message(chat_id=chat.id, text=text)
    except ZeroDivisionError:
        context.bot.send_message(chat_id=chat.id, text='Division by zero!')
    except (NameError, SyntaxError):
        context.bot.send_message(chat_id=chat.id, text='Invalid input!!!')


disp = updater.dispatcher
disp.add_handler(CommandHandler('start', start))
disp.add_handler(MessageHandler(Filters.all, reply_message))

updater.start_polling()
updater.idle()
