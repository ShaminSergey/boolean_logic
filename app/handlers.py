from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)
