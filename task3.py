import telebot
from telebot import types
import requests
import time

bot = telebot.TeleBot('TOKEN')

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_reg = types.KeyboardButton('Регистрация')
btn_alarm = types.KeyboardButton('Тревога')
markup.add(btn_reg, btn_alarm)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Здравствуй, {message.from_user.first_name}! Я бот Альберт',  reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_message(message):
    # print(message)
    data = open('log.txt', mode='a', encoding='utf-8')
    log_text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
    data.write(log_text)
    data.close()
    text = message.text.lower()
    if text == 'регистрация':
        try:
            data = open('registered_users.txt', mode='r', encoding='utf-8')
            id_list = data.readlines()
            data.close()
            print(id_list)
            id_list = list(el[:-1] for el in id_list)
        except:
            data = open('registered_users.txt', mode='w', encoding='utf-8')
            data.close()
        print(id_list)
        if str(message.from_user.id) not in id_list:
            data = open('registered_users.txt', mode='a', encoding='utf-8')
            data.write(f'{message.from_user.id}\n')
            data.close()
            bot.reply_to(message, 'Регистрация прошла успешно!')
        else:
            bot.reply_to(message, 'Вы уже зарегистрированы')
    elif message.text == 'тревога':
        data = open('registered_users.txt', mode='r', encoding='utf-8')
        id_list = data.read().split('\n')
        data.close()
        id_list = id_list[:-1]
        for id in id_list:
            bot.send_message(id, f'{message.from_user.first_name} поднял тревогу')

    elif 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
    elif 'погод' in text:
        req = requests.get('https://wttr.in/?0T?')
        bot.reply_to(message, req.text)

bot.polling()

