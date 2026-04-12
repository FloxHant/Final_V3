import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('8235764815:AAFgCi7Rf7kFNz-_wXVqv-gt2fkJu9yaMmQ') 


def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Расписание"))
    markup.row(KeyboardButton("Помощь"))
    return markup

def days_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Понедельник"), KeyboardButton("Вторник"))
    markup.row(KeyboardButton("Среда"), KeyboardButton("Четверг"))
    markup.row(KeyboardButton("Пятница"))
    return markup

def back_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("Назад"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я телеграм-бот для вашей онлайн-школы. Я помогу вам узнавать, какие уроки у вас завтра.",
        reply_markup=main_menu()
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Если у вас есть какой-либо вопрос, напишите на g-mail"
    )

@bot.message_handler(func=lambda message: message.text == "Помощь")
def help_response(message):
    bot.send_message(
        message.chat.id,
        "Если у вас есть какой-либо вопрос, напишите на g-mail",
        reply_markup=back_button()
    )

@bot.message_handler(func=lambda message: message.text == "Назад")
def go_back(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я телеграм-бот для вашей онлайн-школы. Я помогу вам узнавать, какие уроки у вас завтра.",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: message.text == "Расписание")
def show_schedule(message):
    bot.send_message(
        message.chat.id,
        "Пожалуйста, выберите день, для которого вы хотите увидеть расписание.",
        reply_markup=days_menu()
    )

@bot.message_handler(func=lambda message: message.text in [
    "Понедельник", "Вторник", "Среда", "Четверг", "Пятница"
])
def show_day_schedule(message):
    day = message.text
    schedule_text = f"Расписание на {day}:\n[здесь будет список уроков]"
    bot.send_message(
        message.chat.id,
        schedule_text,
        reply_markup=back_button()
    )

bot.infinity_polling()