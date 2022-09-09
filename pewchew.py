from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from googletrans import Translator

import os

bot = Bot(token='')
dp = Dispatcher(bot)
translator= Translator()
async def onstartup():
    print('Бот работает')

mode=1
b3=KeyboardButton('/uz')
b1=KeyboardButton('/en')
b2=KeyboardButton('/ru')
client_1=ReplyKeyboardMarkup(resize_keyboard=True)
client_1.add(b3,b1,b2)


  

@dp.message_handler(commands=['help','start'])
async def help(message : types.Message):
    global mode
    mode=0
    await bot.send_message(message.from_user.id, 'Men tarjimonman, qaysi tilga tarjima qilay?',reply_markup= client_1)
    await bot.send_message(message.from_user.id, 'Я переводчик, на какой язык переводить?')
    await bot.send_message(message.from_user.id, 'I am a translator, into what language should I translate?')
    
@dp.message_handler(commands=['credits'])
async def help(message : types.Message):
    await bot.send_message(message.from_user.id, 'creator @aziz_johny')   




@dp.message_handler(commands=['uz','en','ru'])
async def helper(message : types.Message):
    global mode
    if message.text=='/en':
        mode=1
    elif message.text=='/uz':
        mode=2
    elif message.text=='/ru':
        mode=3
    
           
 

                


    
@dp.message_handler()
async def translation_en(sentences : types.Message):
    global mode
    if mode==1:
        text_org=sentences.text
        result_of_translation = translator.translate(text_org,dest='en')
        await sentences.reply(result_of_translation.text,reply_markup= client_1)
        mode=0      
    elif mode==2:
        text_org=sentences.text
        result_of_translation = translator.translate(text_org,dest='uz')
        await sentences.reply(result_of_translation.text,reply_markup= client_1) 
        mode=0
    elif mode==3:
        text_org=sentences.text
        result_of_translation = translator.translate(text_org,dest='ru')
        await sentences.reply(result_of_translation.text,reply_markup= client_1)
        mode=0
    elif mode == 0:
        mode=0
        await bot.send_message(sentences.from_user.id, 'Til tanlang',reply_markup= client_1)
        await bot.send_message(sentences.from_user.id, 'Выберите язык')
        await bot.send_message(sentences.from_user.id, 'Choose a language')


   
    






if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)