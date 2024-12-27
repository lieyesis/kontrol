import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")


from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers.config import BOT_TOKEN
from bot.handlers import start, complaint
from bot.database import init_db

def main():
    init_db()
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(complaint.router)

    dp.run_polling(bot)

if __name__ == "__main__":
    main()
