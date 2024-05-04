import aiogram.types as aiogram_types
from aiogram import Router
from aiogram.filters import Command, CommandStart

from src.messages.management import HELP_MSG, START_MSG

router = Router()


@router.message(CommandStart())
async def start(message: aiogram_types.Message):
    await message.answer(START_MSG)


@router.message(Command("help"))
async def help(message: aiogram_types.Message):
    await message.answer(HELP_MSG)
