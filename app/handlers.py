from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)


@router.message(F.text == 'Логические вентили')
async def log_ven(message: Message):
    await message.answer("Логические вентили,отличный выбор!")


@router.message(F.text == 'Логические блоки')
async def log_ven(message: Message):
    await message.answer("Логические блоки,отличный выбор!")


@router.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Привет!')
