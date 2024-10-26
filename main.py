import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN, DATABASE
from logik import SupportBotLogic

bot = telebot.TeleBot(TOKEN)

logic = SupportBotLogic(DATABASE)

# Создаем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_start = KeyboardButton("start")
button_help = KeyboardButton("help")
keyboard.add(button_start, button_help)

# start в начале
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Выберите одну из опций:", reply_markup=keyboard)

# help с кнопки
@bot.message_handler(func=lambda message: message.text == "help")
def send_help(message):
    bot.reply_to(message, "Напишите имя на английском, с большой буквы.", reply_markup=keyboard)

# start с кнопки
@bot.message_handler(func=lambda message: message.text == "start")
def handle_start(message):
    bot.reply_to(message, "Выберите опцию или напишите имя:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    name = message.text
    response = logic.get_family_info(name)
    
    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.polling(none_stop=True)