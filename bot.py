from aiogram import executor
from loader import dp

from tg_bot import middleware
from tg_bot import filters
from tg_bot import handlers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
