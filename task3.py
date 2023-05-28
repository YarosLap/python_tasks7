import telebot
import random
count = 0
a = random.randint(1,1000)

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Здравствуй, {message.from_user.first_name}! Угадай число от 1 до 1000')

@bot.message_handler(content_types=['text'])
def text_message(message):
    global count
    b = int(message.text)
    count += 1
    if b<a:
        bot.reply_to(message, 'Больше')
    elif b>a:
        bot.reply_to(message, 'Меньше')
    else:
        bot.reply_to(message, f'Угадали за {count} попыток')

bot.polling()

