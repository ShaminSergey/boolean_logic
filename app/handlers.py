from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}', reply_markup=kb.main)


@router.message(Command("clear"))
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        # Если сообщение не найдено (уже удалено или не существует),
        # код ошибки будет "Bad Request: message to delete not found"
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")


@router.message(F.text == 'Логические вентили')
async def log_ven(message: Message):
    file_or = FSInputFile("./app/image/OR-gate.gif")
    file_and = FSInputFile("./app/image/AND.gif")
    await message.answer_animation(animation=file_or, caption='Вентиль - ИЛИ')
    await message.answer_animation(animation=file_and, caption='Вентиль - И')


@router.message(F.text == 'Логические блоки')
async def log_block(message: Message):
    await message.answer("Логические блоки,отличный выбор!")


@router.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Привет!')
