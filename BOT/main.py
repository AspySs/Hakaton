import telebot
import time
# Токен, который выдает @botfather
bot = telebot.TeleBot('5690661059:AAEtuZiAni00e3dKN5yKR45RCbrVdAPOcVc')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@buznews'
# Загружаем список шуток
bot.send_message(CHANNEL_NAME, "test")
# Делаем паузу в один час
time.sleep(3600)