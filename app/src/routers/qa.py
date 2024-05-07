import aiogram.types as aiogram_types
from aiogram import Router
from aiogram.utils.chat_action import ChatActionSender

from src.utils.llm import generate
from src.utils.retriever import retrieve

router = Router()


@router.message()
async def answer(message: aiogram_types.Message):
    async with ChatActionSender.typing(bot=message.bot, chat_id=message.chat.id):
        information = await retrieve(message.text)
        response = await generate(message.text, information)

    await message.answer(response)
