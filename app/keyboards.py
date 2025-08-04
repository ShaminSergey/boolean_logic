from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Логические вентили')],
    [KeyboardButton(text='Логические блоки')]
], resize_keyboard=True)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подробнее...', callback_data='more')]
])
