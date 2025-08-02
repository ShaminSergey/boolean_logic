from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Логические вентили')],
    [KeyboardButton(text='Логические блоки')],
    [KeyboardButton(text='Назад')]
], resize_keyboard=True)

