import telebot
from telebot import types
from telebot.types import Message
import requests
from bs4 import BeautifulSoup as bs
import re
import datetime

#-------------------------------------------------------------------------------
idea1 = [30]#256370991
idea = [8]#544463656
ID = []
#-------------------------------------------------------------------------------
TOKEN = '1007184768:AAFjwERR1Mz0KinRny5EkTh7FVR9EnV4cI4'
bot = telebot.TeleBot(TOKEN)
#-------------------------------------------------------------------------------
headers = {'accept': '*/*' , 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
base_url = 'https://mover.uz/video/anime/'
#-------------------------------------------------------------------------------
#ID = open('ID.txt', 'w')

@bot.message_handler(commands=['start'])
def welcome(message):
    #ID.write(str(message.chat.id))
    #sti = open('C1.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)
    ID.insert(0,message.chat.id)
    markup =  types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Продолжить ➡️", callback_data='next')
    markup.add(button1)
    bot.send_message(ID[0], "Добро пожаловать!", reply_markup=markup)
    bot.send_message(256370991, ID[0])
    #ID.close()


@bot.callback_query_handler(func=lambda call: True)
def welcome_first(call):
    if call.data == 'next':
        markup =  types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Музыка", callback_data='music')
        button2 = types.InlineKeyboardButton("Аниме", callback_data='anime')
        button3 = types.InlineKeyboardButton("Будильник", callback_data='clock')
        markup.add(button1,button2)
        markup.add(button3)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите один из разделов:", reply_markup=markup)
    elif call.data == 'music':
        markup2 =  types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Рэп",callback_data='but1')
        button2 = types.InlineKeyboardButton("Поп-музыка",callback_data='but2')
        button3 = types.InlineKeyboardButton("Электронная музыка",callback_data='but3')
        button4 = types.InlineKeyboardButton("Зарубежная",callback_data='but4')
        button5 = types.InlineKeyboardButton("Топ-40 музыки",callback_data='but5')
        button6 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup2.add(button1, button2)
        markup2.add(button3, button4)
        markup2.add(button5)
        markup2.add(button6)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="🎧Выберите интересующую Вас тематику:🎧", reply_markup=markup2)


    elif call.data == 'back':
        markup1 =  types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Музыка", callback_data='music')
        button2 = types.InlineKeyboardButton("Аниме", callback_data='anime')
        button3 = types.InlineKeyboardButton("Будильник", callback_data='clock')
        markup1.add(button1,button2)
        markup1.add(button3)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите один из разделов:", reply_markup=markup1)
    elif call.data == 'anime':
        tims = []
        tims1 = []
        def mover_parse(headers, base_url):
            session = requests.Session()
            request = session.get(base_url, headers=headers)
            if request.status_code == 200:
                soup = bs(request.content, 'html.parser')
                divs = soup.find_all('div', attrs = {'class': 'video s'})
                for b in divs:
                    title = b.find('a')
                                    #link = b.get('title')
                                    #print (title)
                    tims.append(title)
                t = 1
                for element in tims:
                    name = element.get('title')
                    full_name = str( str(t)+ ") " + name)
                    link = str(element.get('href'))
                    full_link = str("https://mover.uz" + link)

                    tims1.append( full_name)
                    tims1.append( full_link)
                    t += 1

                markupMOVER = types.InlineKeyboardMarkup()

                markupMOVER.add( types.InlineKeyboardButton(text = tims1[0], url = tims1[1]), types.InlineKeyboardButton(text = tims1[2], url = tims1[3]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[4], url = tims1[5]), types.InlineKeyboardButton(text = tims1[6], url = tims1[7]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[8], url = tims1[9]), types.InlineKeyboardButton(text = tims1[10], url = tims1[11]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[12], url = tims1[13]), types.InlineKeyboardButton(text = tims1[14], url = tims1[15]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[16], url = tims1[17]), types.InlineKeyboardButton(text = tims1[18], url = tims1[19]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[20], url = tims1[21]), types.InlineKeyboardButton(text = tims1[22], url = tims1[23]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[24], url = tims1[25]), types.InlineKeyboardButton(text = tims1[26], url = tims1[27]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[28], url = tims1[29]), types.InlineKeyboardButton(text = tims1[30], url = tims1[31]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[32], url = tims1[33]), types.InlineKeyboardButton(text = tims1[34], url = tims1[35]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[36], url = tims1[37]), types.InlineKeyboardButton(text = tims1[38], url = tims1[39]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[40], url = tims1[41]), types.InlineKeyboardButton(text = tims1[42], url = tims1[43]))
                markupMOVER.add( types.InlineKeyboardButton(text = tims1[44], url = tims1[45]), types.InlineKeyboardButton(text = tims1[46], url = tims1[47]))
                markupMOVER.add( types.InlineKeyboardButton(text = "⬅️ Вернуться к меню", callback_data = 'back'))

                bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="🍿🍿Список онгоингов, нажмите, чтобы посмотреть:🍿🍿", reply_markup=markupMOVER)
                                #bot.send_message(message.chat.id, "Нажмите чтобы посмотреть онгоинг: ", reply_markup=markupMOVER)
            else:
                print ("no")

        mover_parse(headers, base_url)

    elif call.data == 'clock' or call.data=='one_one':
        markup4 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup4.add(button1,button2,button3)
        markup4.add(button4,button5,button6)
        markup4.add(button7)
        markup4.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup4)



    elif call.data == 'minus_one':
        idea.insert(0,idea[0]-1)
        markup5 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one_sec')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup5.add(button1,button2,button3)
        markup5.add(button4,button5,button6)
        markup5.add(button7)
        markup5.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup5)

    elif call.data == 'minus_one_sec':
        idea.insert(0,idea[0]-1)
        markup6 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup6.add(button1,button2,button3)
        markup6.add(button4,button5,button6)
        markup6.add(button7)
        markup6.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup6)

    elif call.data == 'plus_one':
        idea.insert(0,idea[0]+1)
        markup7 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one_sec')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup7.add(button1,button2,button3)
        markup7.add(button4,button5,button6)
        markup7.add(button7)
        markup7.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup7)

    elif call.data == 'plus_one_sec':
        idea.insert(0,idea[0]+1)
        markup8 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup8.add(button1,button2,button3)
        markup8.add(button4,button5,button6)
        markup8.add(button7)
        markup8.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup8)

    elif call.data == 'minus_five':
        idea1.insert(0,idea1[0]-5)
        markup9 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five_sec')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup9.add(button1,button2,button3)
        markup9.add(button4,button5,button6)
        markup9.add(button7)
        markup9.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup9)

    elif call.data == 'minus_five_sec':
        idea1.insert(0,idea1[0]-5)
        markup10 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup10.add(button1,button2,button3)
        markup10.add(button4,button5,button6)
        markup10.add(button7)
        markup10.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup10)

    elif call.data == 'plus_five':
        idea1.insert(0,idea1[0]+5)
        markup11 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five_sec')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup11.add(button1,button2,button3)
        markup11.add(button4,button5,button6)
        markup11.add(button7)
        markup11.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup11)

    elif call.data == 'plus_five_sec':
        idea1.insert(0,idea1[0]+5)
        markup12 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⏪-1", callback_data='minus_one')
        button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
        button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
        button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
        button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
        button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
        button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
        button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup12.add(button1,button2,button3)
        markup12.add(button4,button5,button6)
        markup12.add(button7)
        markup12.add(button8)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup12)

    elif call.data == 'ready':
        markup13 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
        markup13.add(button1)
        bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text=("Бот пришлет сообщение в "+str(idea[0])+":"+str(idea1[0])+" ⏰"), reply_markup=markup13)
        while True:
            b = datetime.datetime.now()
            c = datetime.datetime(b.year, b.month, b.day, b.hour, b.minute)
            a = datetime.datetime(b.year, b.month, b.day, idea[0] - 3, idea1[0])
            if a == c:
                bot.send_message(ID[0], "🔔🔔🔔 ПОДЪЕМ, ВРЕМЯ ВСТАВАТЬ!!! 🔔🔔🔔")
                bot.send_message(544463656, "Мама привет!")
                break
    # elif call.data == 'minus_five':
    #     idea1.insert(0,idea1[0]-5)
    #     clock_func(idea,idea1,call)
    #
    # elif call.data == 'plus_five':
    #     idea1.insert(0,idea1[0]+5)
    #     markup8 =  types.InlineKeyboardMarkup()
    #     button1 = types.InlineKeyboardButton("⏪-1", callback_data='one_one')
    #     button2 = types.InlineKeyboardButton(str(idea[0]) + " часов", callback_data='text')
    #     button3 = types.InlineKeyboardButton("⏩+1", callback_data='plus_one')
    #     button4 = types.InlineKeyboardButton("⏪-5", callback_data='minus_five')
    #     button5 = types.InlineKeyboardButton(str(idea1[0]) + " минут", callback_data='text')
    #     button6 = types.InlineKeyboardButton("⏩+5", callback_data='plus_five')
    #     button7 = types.InlineKeyboardButton("Готово!", callback_data='ready')
    #     button8 = types.InlineKeyboardButton("⬅️ Вернуться к меню", callback_data='back')
    #     markup8.add(button1,button2,button3)
    #     markup8.add(button4,button5,button6)
    #     markup8.add(button7)
    #     markup8.add(button8)
    #     bot.edit_message_text(chat_id=ID[0], message_id=call.message.message_id, text="Выберите время для работы:", reply_markup=markup8)
    #     idea1.insert(0,idea1[0]+5)

        # bot.edit_message_replyMarkup(chat_id=call.message.chat.id, message_id=call.message.message_id,
        #     reply_markup=reply_markup,
        #                    *args, **kwargs)
        # markup =  types.InlineKeyboardMarkup()
        # button1 = types.InlineKeyboardButton("Музыка", callback_data='music')
        # button2 = types.InlineKeyboardButton("Игры", callback_data='games')
        # markup.add(button1,button2)
        # bot.send_message(ID[0], "пункты ---->>>", reply_markup=markup)

# bot.send_message(ID[0], "Добро пожаловать, ID[0]!")



# b = datetime.datetime.now()
# a = datetime.datetime(2020, 2, 6, 19, 50)



# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.data == 'music':
#         bot.send_message(ID, "working step music")
#     elif call.data == 'games':
#         bot.send_message(ID, "working step games")

bot.polling(none_stop=True)
