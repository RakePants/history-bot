import aiogram.types as aiogram_types
from aiogram import Router

router = Router()


@router.message()
async def answer(message: aiogram_types.Message):
    await message.answer(message.text)
