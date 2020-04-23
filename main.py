#! /usr/bin/env python
# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher, types, executor
from googletrans import Translator

import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument('token')
args = parser.parse_args()
token = args.token

bot = Bot(token=token)
dp = Dispatcher(bot)
trans = Translator()


def weird_trans(text):
    lang_list = ['hy', 'ar', 'uz', 'kk', 'ru']
    for lang in lang_list:
        text = trans.translate(text, dest=lang).text
    return text


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Отправь мне любую фразу, я прогоню ее через несколько переводов '
                        'Google Translate и отправлю результат. Автор: @egorvoron')


@dp.message_handler()
async def send_trans(message: types.Message):
    try:
        if len(message.text) >= 1000:
            await message.reply('Извините, входной текст слишком длинный, отправьте текст менее 1000 символов длиной')
            return
        await message.reply(weird_trans(message.text))
    except Exception as ex:
        print(ex)
        await message.reply('Извините, неизвестная ошибка(')


if __name__ == '__main__':
    print('Starting at', datetime.now() + timedelta(hours=+3))
    executor.start_polling(dp, skip_updates=True)
