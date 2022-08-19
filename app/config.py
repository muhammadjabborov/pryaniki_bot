from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5767830832:AAG6DgXqR8ZZFI9eH9hThfM8zahp-WEz5zI')
dp = Dispatcher(bot, storage=storage)

