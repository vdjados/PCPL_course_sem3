from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                    [KeyboardButton(text='Корзина')],
                                    [KeyboardButton(text='Контакты')],
                                    [KeyboardButton(text='О нас')]
                                    ])

catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки', callback_data='Shirts')],
                                                [InlineKeyboardButton(text='Кроссовки', callback_data='Snickers')],
                                                [InlineKeyboardButton(text='Кепки', callback_data='Caps')]])