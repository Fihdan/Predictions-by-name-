#import telebot
from telebot import types, TeleBot
from config import TOKEN_TELEGRAM
from geo import g
import json
import datetime
#import collections
from api_s import ex

bot = TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(commands=["start"])
def start (message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Для начала работы с ботом необходимо отправить геолокацию", reply_markup=keyboard)

@bot.message_handler(content_types=['location'])
def location (message):
    if message.location is not None:
        print(message.location.longitude, message.location.latitude)
        print(g(message.location.longitude, message.location.latitude))
        ge =  g(message.location.longitude, message.location.latitude)['address']
        global p
        p = f"{ge['country']}, {ge['state']}, {ge['city_district']}, {ge['road']}, {ge['house_number']}"
        bot.send_message(message.chat.id, p)
        mesg = bot.send_message(message.chat.id, 'Это верный адрес?(Если верный напишите "Адрес верный". а если нет то, введите свой действующий адрес)')
        bot.register_next_step_handler(mesg, step)
def step(message):
    global data
    with open("data.json", encoding="utf-8") as file:
        data = json.load(file)
    with open("data.json", "w", encoding="utf-8") as file:
        if message.text == "Адрес верный":
            if not message.chat.id in data:
                data[message.chat.id] = {
                    f"{datetime.datetime.strftime('%d.%m.%Y %I:%M:%s')}" : {
                        "first_name" : f"{message.from_user.first_name}",
                        "last_name" : f"{message.from_user.last_name}",
                        "username" : f"{message.from_user.username}",
                        "adres_nas" : f"{p}",
                        "adres_pol" : f"{p}"
                    }
                }
            else:
                data[message.chat.id][f"{datetime.datetime}"] = {
                        "first_name" : f"{message.from_user.first_name}",
                        "last_name" : f"{message.from_user.last_name}",
                        "username" : f"{message.from_user.username}",
                        "adres_nas" : f"{p}",
                        "adres_pol" : f"{p}"
                    }
        else:
            if not message.chat.id in data:
                data[message.chat.id] = {
                    f"{datetime.datetime}" : {
                        "first_name" : f"{message.from_user.first_name}",
                        "last_name" : f"{message.from_user.last_name}",
                        "username" : f"{message.from_user.username}",
                        "adres_nas" : f"{p}",
                        "adres_pol" : f"{message.text}"
                    }
                }
            else:
                data[message.chat.id][f"{datetime.datetime}"] = {
                        "first_name" : f"{message.from_user.first_name}",
                        "last_name" : f"{message.from_user.last_name}",
                        "username" : f"{message.from_user.username}",
                        "adres_nas" : f"{p}",
                        "adres_pol" : f"{message.text}"
                    }
        file.write(json.dumps(data))

@bot.message_handler(content_types=['text'])
def text(message):
    #[last] = collections.deque(data[message.chat.id], maxlen=1)
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    if message.chat.id in data:
        mes = bot.send_message(message.chat.id, "Введите имя по которому хотите получить предсказания(имя необходимо вводить транслитом, Иван = Ivan)")
        def func(message):
            bot.send_message(message.chat.id, ex(message.text))
        bot.register_next_step_handler(mes, func)
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
        keyboard.add(button_geo)
        bot.send_message(message.chat.id, "В так и не отправили свою геолокацию, а она необходима для начала работы", reply_markup=keyboard)


bot.infinity_polling()