from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Логический вентиль "НЕ"'),
     KeyboardButton(text='Логический вентиль "И"'),],

    [KeyboardButton(text='Логический вентиль "ИЛИ"'),
     KeyboardButton(text='Логический вентиль "НЕ И (И-НЕ)"')],

    [KeyboardButton(text='Логический вентиль "НЕ ИЛИ (ИЛИ-НЕ)"'),
     KeyboardButton(text='Логический вентиль "Исключающее ИЛИ"')],

    [KeyboardButton(text='Логический вентиль "Исключающее ИЛИ с инверсией"')]
], resize_keyboard=True)

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подробнее...', callback_data='more')]
])
