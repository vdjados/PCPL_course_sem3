import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token='7246592705:AAE13GPoAR4n40658kx3vm8G-A_bQzcf4T8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')