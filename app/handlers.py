from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
import app.keyboards as kb

router = Router()

msg_help = 'Бот создан для начинающих любителей логической электроника'

affiliation = ['ГОСТ', 'EUROPA', 'USA']

file_or = [FSInputFile("./app/image/logic gate/or/OR_gate_RU.jpg"),
           FSInputFile("./app/image/logic gate/or/IEC_OR_label.jpg"),
           FSInputFile("./app/image/logic gate/or/Or-gate-en.jpg")]


file_and = FSInputFile("./app/image/AND.gif")


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)


@router.message(F.text == 'Логический вентиль "ИЛИ"')
async def log_or(message: Message):
    for i in range(3):
        await message.answer_animation(animation=file_or[i], caption=f'Вентиль - "ИЛИ" по {affiliation[i]}')


@router.message(Command('help'))
async def cmd_clear(message: Message):
    await message.answer(msg_help)
