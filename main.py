from aiogram import executor
from app.handars import dp

if __name__ == '__main__':
    executor.Executor(dp, skip_updates=True).start_polling()
