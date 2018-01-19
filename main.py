from pagescan.page import BaraholkaPage
from sectionscan.section_scanning import get_goods_urls

import telebot
import threading
import time

TOKEN = "494320620:AAEGN18JQyY45P8oDO4Wi0VuV4Hb4rqNh78"
CHAT_ID = "270380442"

bot = telebot.TeleBot(TOKEN)

urls = get_goods_urls("https://baraholka.onliner.by/search.php?q=ps+4+slim&f=&topicTitle=1")

ps4s = []

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if "Give" in message.text or "Дай" in message.text:
        for url in urls:
            bot.send_message(message.chat.id, url)
            print(message.chat.id)


def find_all():
    urls = get_goods_urls("https://baraholka.onliner.by/search.php?q=ps+4+slim&f=&topicTitle=1")

    for url in urls:
        ps4 = BaraholkaPage()
        ps4.download(url)
        if ps4.data() not in map(lambda x: x.data(), ps4s):

            bot.send_message(CHAT_ID, "Found new PS 4 Slim!")
            bot.send_message(CHAT_ID, ps4.data().name)
            bot.send_message(CHAT_ID, "\t" + ps4.data().cost + " BYN")
            bot.send_message(CHAT_ID, "\t" + ps4.data().description)
            bot.send_message(CHAT_ID, url)

            print("Found new PS 4 !")
            ps4s.append(ps4)
            print(ps4.data().name)
            print("\t", ps4.data().cost, "BYN")
            print("\t", ps4.data().description)
            print("\t", ps4.data().url)

    return urls


def run_telebot():
    bot.polling(none_stop=True)

if __name__ == '__main__':

    threading.Thread(target=run_telebot, daemon=True).start()
    print("Bot has been started")

    while True:
        find_all()
        time.sleep(1)

