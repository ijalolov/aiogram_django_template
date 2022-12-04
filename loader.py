import logging
from environ import Env
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_config.settings")
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")
django.setup()

env = Env()
env.read_env('.env')

BOT_TOKEN = env.str('BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [int(admin) for admin in env.str('ADMINS').split(',')]
