from telebot import TeleBot , types
#from dotenv import load_dotenv
import random

TOKEN = "8788454171:AAE2OjIglW2LvL4nrxWPaOUgoTyYpU-OJsM"

MOM_SENTENCE = []
DAD_SENTENCE = []
PARTNER_SENTENCE = []
WIFE_SENTENCE = []
HUSBAND_SENTENCE = []

bot = TeleBot(TOKEN)

def languege(lang):
    if lang == "en":
        return True
    elif lang == "fa":
        return False
        

@bot.message_handler(commands=['start','help'])
def welcome(message):
    if message.text == '/start':
        btns = [
            [types.InlineKeyboardButton("English", callback_data="en")],
            [types.InlineKeyboardButton("فارسی", callback_data ="fa")]
        ]
        markup = types.InlineKeyboardMarkup(btns)
        
        bot.send_message(message.chat.id, "Hello! Welcome to the beatiful sentences bot choose one of the options" \
        "\n سلام به بات جملات زیبا خوش آمدید یکی از گزینه های زیر را انتخاب کنید", markup=markup)

    elif message.text == "/help":
        bot.send_message(message.chat.id, "This bot is desined to send you a random beatiful sentence in English or Persian. " \
        "\n این بات برای ارسال جملات زیبا به زبان انگلیسی و فارسی طراحی شده است")


@bot.callback_query_handler(func=lambda call: call.data in ["en", "fa"])
def start(call):
    global lan
    btns_en = [
        [types.InlineKeyboardButton("Add sentence", callback_data="add")],
        [types.InlineKeyboardButton("Get sentence", callback_data="get")]
    ]

    btns_fa = [
        [types.InlineKeyboardButton("افزودن جمله", callback_data="add")],
        [types.InlineKeyboardButton("دریافت جمله", callback_data="get")]
    ]

    if call.data == "en":
        lan = "en"
        markup = types.InlineKeyboardMarkup(btns_en)
        bot.send_message(call.message.chat.id, "You have selected English. Please choose one of the options below", markup=markup)

    elif call.data == "fa":
        lan = "fa"
        markup = types.InlineKeyboardMarkup(btns_fa)
        bot.send_message(call.message.chat.id, "شما زبان فارسی را انتخاب کرده اید. لطفا یکی از گزینه های زیر را انتخاب کنید ", markup=markup)


if languege(lan):
    @bot.callback_query_handler(func=lambda call: call.data in ["add", "get"], commands=['add', 'get'])
    def action(call):
        btns = ['Mother', 'Father', 'Wife', 'Husband', 'Partner', 'back']
        
        for btn in btns:
            markup.add(btn)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        if call.data == "add":
            bot.send_message(call.message.chat.id, "please send me the sentence you want toa add" \
            "\nfor which category do you want to add the sentence?", reply_markup=markup) 


    @bot.message_handler(func=lambda x: x in ['Mother', 'Father', 'Wife', 'Husband', 'Partner'])   
    def sentence(message):
        if message.text == 'Mother':
            if len(MOM_SENTENCE) == 0:
                bot.send_message(message.chat.id, "I'm sorry, I don't have any sentences right now \nif you have or know some sentences please /add")
            else:
                bot.send_message(message.chat.id, random.choice(MOM_SENTENCE))
        elif message.text == 'Father':
            if len(DAD_SENTENCE):
                bot.send_message(message.chat.id, "I'm sorry, I don't have any sentences right now \nif you have or know some sentences please /add")
            else:     
                bot.send_message(message.chat.id, random.choice(DAD_SENTENCE))
        elif message.text == 'Wife':
            if len(WIFE_SENTENCE):
                bot.send_message(message.chat.id, "I'm sorry, I don't have any sentences right now \nif you have or know some sentences please /add")
            else:
                bot.send_message(message.chat.id, random.choice(WIFE_SENTENCE))
        elif message.text == 'Husband':
            if len(HUSBAND_SENTENCE):
                bot.send_message(message.chat.id, "I'm sorry, I don't have any sentences right now \nif you have or know some sentences please /add")
            else:
                bot.send_message(message.chat.id, random.choice(HUSBAND_SENTENCE))
        elif message.text == 'Partner':
            if len(PARTNER_SENTENCE):
                bot.send_message(message.chat.id, "I'm sorry, I don't have any sentences right now \nif you have or know some sentences please /add")
            else:
                bot.send_message(message.chat.id, random.choice(PARTNER_SENTENCE))


else:
    @bot.callback_query_handler(func=lambda call: call.data in ["add", "get"], commmands=['add', 'get'])
    def action_en(call):
        btns = ['مادر', 'پدر', 'همسر', 'شوهر', 'پارتنر']
        
        for btn in btns:
            markup.add(btn)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        if call.data == "add":
            bot.send_message(call.message.chat.id, "لطفا از گزینه های زیر شخصی که این جمله را بهش تقدیم میکنید انتخاب کنید", reply_markup=markup)


    @bot.message_handler(func=lambda x: x in ['مادر', 'پدر', 'همسر', 'شوهر', 'پارتنر'])
    def action_fa(message):
        if message.text == 'مادر':
            bot.send_message(message.chat.id, random.choice(MOM_SENTENCE))
        elif message.text == 'پدر':
            bot.send_message(message.chat.id, random.choice(DAD_SENTENCE))
        elif message.text == 'همسر':
            bot.send_message(message.chat.id, random.choice(WIFE_SENTENCE))
        elif message.text == 'شوهر':
            bot.send_message(message.chat.id, random.choice(HUSBAND_SENTENCE))
        elif message.text == 'پارتنر':
            bot.send_message(message.chat.id, random.choice(PARTNER_SENTENCE))


bot.polling()