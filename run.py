import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from app.handlers import router
load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT!!!')

