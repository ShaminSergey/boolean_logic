from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
import app.keyboards as kb

router = Router()

msg_help = 'Бот создан для начинающих любителей логической электроника'
file_or = FSInputFile("./app/image/OR-gate.gif")
file_and = FSInputFile("./app/image/AND.gif")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)


@router.message(F.text == 'Логические вентили')
async def log_ven(message: Message):
    await message.answer_animation(animation=file_or, caption='Вентиль - ИЛИ')
    await message.answer_animation(animation=file_and, caption='Вентиль - И')


@router.message(F.text == 'Логические блоки')
async def log_block(message: Message):
    await message.answer("Логические блоки,отличный выбор!")


@router.message(Command('help'))
async def cmd_clear(message: Message):
    await message.answer(msg_help)
