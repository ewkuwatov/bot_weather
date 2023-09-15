import telebot
import requests
import json

bot = telebot.TeleBot('6003086200:AAFoOE-hqh8iSpZokH3sAPbyl4i0pcRu8SE')
API = '251d5abef39b9afe82e8395cd51cba45'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, выбери свой город или напиши его!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&cnt=7&appid={API}')
    data = res.json()
    print(data)
    bot.reply_to(message, f'Cейчас погода: {data["main"]["temp"]}°C')



bot.polling(none_stop=True)

