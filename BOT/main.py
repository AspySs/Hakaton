import time
from telegram.ext import Updater, MessageHandler, Filters
import sqlite3

conn = sqlite3.connect('../data.sqlite', check_same_thread=False)
cur = conn.cursor()


KEY = "5690661059:AAEtuZiAni00e3dKN5yKR45RCbrVdAPOcVc"
updater = Updater(token=KEY, use_context=True)
dispatcher = updater.dispatcher


def forwarder(update, context):
    msg = update.channel_post
    tag_source = msg.text
    tags = {tag.strip("#") for tag in tag_source.split() if tag.startswith("#")}

    c = cur.execute("""INSERT INTO posts VALUES (NULL, ?, ?)""", (msg.text, time.time()))
    id_post = c.lastrowid
    conn.commit()

    for t in tags:
        cur.execute("INSERT INTO tags VALUES (NULL, ?, ?, ?)", (id_post, t, time.time()))
        conn.commit()



forwardHandler = MessageHandler(Filters.text & (~Filters.command), forwarder)
dispatcher.add_handler(forwardHandler)
updater.start_polling()
updater.idle()
conn.close()