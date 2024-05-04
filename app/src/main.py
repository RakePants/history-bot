import asyncio

from aiogram import Bot, Dispatcher
from routers import management, qa

from src.config import settings

dp = Dispatcher()


async def main():
    bot = Bot(settings.bot_token)

    dp.include_router(management.router)
    dp.include_router(qa.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
