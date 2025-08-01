from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}')
