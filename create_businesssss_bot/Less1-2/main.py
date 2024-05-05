import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard
from random_fox import fox


# Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['старт']))
@dp.message(Command(commands=['start']))
@dp.message(F.text.lower() == 'старт')
@dp.message(F.text.lower() == 'start')
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}, я милый бот, которого сделала Римма! Чтобы проверить меня напиши в чат: '
                         f' старт, пока, инфо, на английском или русском языке. Буквы могут быть большими или маленькими, бот все равно поймет тебя. '
                         f'Так же он ответит тебе на : Как дела? и Привет.'
                         f' Ещё попробуй пожалуйста нажать на кнопки внизу, они тоже должны работать', reply_markup=keyboard)


@dp.message(Command(commands=['пока']))
@dp.message(Command(commands=['Bye']))
@dp.message(F.text.lower() == 'пока')
@dp.message(F.text.lower() == 'Bye')
async def stop(message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'Всего хорошего, {message.chat.first_name}!')


@dp.message(Command(commands=['инфо', 'info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(110, 200)
    await message.answer(f'Привет, пусть сегодня тебе подарят: {number} роз!')

@dp.message(F.text.lower() == 'покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)
    img_fox = fox()
    await bot.send_photo(message.from_user.id, img_fox)

@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'как дела' in message.text.lower():
        await message.reply('Не хочу вас расстраивать, но у меня все отлично!')
    else:
        await message.reply('Пока не понимаю вас...')


