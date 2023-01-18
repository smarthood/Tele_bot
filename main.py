'''
Developer: @smarthood

'''

import threading
import time
import datetime
import random


import telegram.ext
from logging import basicConfig, getLogger, INFO

basicConfig(level=INFO)
log = getLogger()


def start(update,context):
    update.message.reply_text("Hello Friends!")
    update.message.reply_text("Type /list to see all Birthday 🎉")
    global USER_ID
    USER_ID=update.message.chat_id

def list(update,context):
    for _ in BDICT:
        update.message.reply_text(BDICT[_]+"-"+_)

def ctime(update,context):
    current_time = datetime.datetime.now()
    now=current_time.strftime("%H:%M:%S")
    update.message.reply_text(now)

def wish():
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now in ("01:00:10" ,"01:00:11"):
            updater.bot.send_message(chat_id=1313787079,text="Good Morning  ☀️ ")
            updater.bot.send_message(chat_id=1313787079,text=f"Have a {random.choice(stwish)} day!")
            for _ in BDICT:
                if CDATE==_[-5:]:
                    byear=int(CYEAR)-int(_[:2])+1
                    updater.bot.send_message(chat_id=-1001434326296,text=f"Happy {byear}st Birthday to you, {BDICT[_]} ✨ ")
            for i in CDICT:
                if CDATE==i[-5:]:
                    updater.bot.send_message(chat_id=-1001434326296,text=f"Happy {CDICT[i]}  ")
            
def main():
    token="5921202727:AAE4ggw1IaX9MP2eNhYcEmcD7YI2D7bVywo"
    today = datetime.datetime.today().strftime("%y-%m-%d")
    global BDICT,CDATE,CYEAR,stwish,CDICT
    stwish=["wonderful","surprise","fantastic","marvellous","good","hopeful","great","nice","special"]
    CYEAR=today[:2]
    CDATE=today[-5:]
    BDICT={
        "02-07-26":"Bright",
        "03-11-09":"Newton",
        "02-05-02":"Shan",
        "02-09-11":"Divain",
        "04-03-14":"Jones",
        "01-04-14":"Jebastin",
        "04-04-14":"Greats",
        "03-09-19":"Kabilan",
        "01-11-18":"Dickson",
        "01-11-09":"Renith",
        }
    CDICT={
    "23-01-01":"New Year 🎆",
    "23-12-25":"christmas 🎄",
    "23-01-15":"pongal 🌤️",
    "23-02-14":"Valentine's Day 💕",
    "23-03-08":"Holi 🎨",
    "23-04-09":"Easter 🕯️",
    "23-11-10":"Diwali 🪔",
    "23-01-26":"Independence Day🇮🇳",
    "23-08-15":"Republic Day 🇮🇳",
    "23-10-02":"Gandhi jeyanthi 🕊️",
    "23-04-22":"Ramzan 🕌",
    "23-01-17":"Test"
    }
    global updater
    updater = telegram.ext.Updater(token,use_context=True)
    disp = updater.dispatcher
    disp.add_handler(telegram.ext.CommandHandler("start",start))
    disp.add_handler(telegram.ext.CommandHandler("list",list))
    disp.add_handler(telegram.ext.CommandHandler("ctime",ctime))
    threading.Thread(target=wish).start()
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
