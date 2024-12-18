from  aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Привет!')
    await message.reply('Добро пожаловать в мой интернет-магазин VladunaShop.')

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('Хорошо, что вы нажали кнопку помощи, но помочь ничем не можем.')

@router.message(F.text == 'Каталог')
async def nice(message:Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)

@router.message(F.text == 'Корзина')
async def nice(message:Message):
    await message.answer('Ваша корзина: ')

@router.message(F.text == 'Контакты')
async def nice(message:Message):
    await message.answer('''При возникновении вопросов, звони по телефону:
+7-914-856-05-43''')

@router.message(F.text == 'О нас')
async def nice(message:Message):
    await message.answer('Вы попали в интернет-магазин VladunaShop, здесь можно приобрести товары на любой вкус и цвет.')

@router.callback_query(F.data == 'Shirts')
async def shirts(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию футболок')

@router.callback_query(F.data == 'Snickers')
async def shirts(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию кроссовок')

@router.callback_query(F.data == 'Caps')
async def shirts(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию кепок')