'''
Developer: @smarthood

'''

import threading
import time
import datetime
import random
import os

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
def wish():
    while True:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now=="06:30:10":
            updater.bot.send_message(chat_id=-1001434326296,text="Good Morning Friends, ☀️ ")
            updater.bot.send_message(chat_id=-1001434326296,text=f"Have a {random.choice(stwish)} day!")
            time.sleep(5)
            for _ in BDICT:
                if CDATE==_[-5:]:
                    byear=int(CYEAR)-int(_[:2])+1
                    updater.bot.send_message(chat_id=-1001434326296,text=f"Happy {byear}st Birthday to you, {BDICT[_]} ✨ ")
            


def main():
    key=os.getenv(token)
    today = datetime.datetime.today().strftime("%y-%m-%d")
    global BDICT,CDATE,CYEAR,stwish
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
    global updater
    updater = telegram.ext.Updater(key,use_context=True)
    disp = updater.dispatcher
    disp.add_handler(telegram.ext.CommandHandler("start",start))
    disp.add_handler(telegram.ext.CommandHandler("list",list))
    threading.Thread(target=wish).start()
    updater.start_polling()
    #updater.idle()

if __name__=='__main__':
    main()
