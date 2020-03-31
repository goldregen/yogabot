# Telegram-Bot
import telegram
import random
import csv 
import numpy

Tokenreader = open("Token.txt","r")
Token = Tokenreader.readline()

bot = telegram.Bot(token=str(Token))

from telegram.ext import Updater
updater = Updater(token=Token, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

print(bot.get_me())  #Gibt Informationen über den Bot aus

#Daten importieren
reader = csv.reader(open("Datenbank.csv", "r"), delimiter=";")
x = list(reader)
data = numpy.array(x).astype("str")
#print(data[13][0])

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please (don't) talk to me (because I'm still in developement)!")

def random_all(update, context):
    if(update.effective_chat.id == 187915045):
        random.seed()
        r = random.choice(data)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Probier's mal mit " + r[1])

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
random_handler = CommandHandler('random',random_all)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)

#updater.start_polling()