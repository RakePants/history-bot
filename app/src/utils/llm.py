from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

from src.config import settings
from src.utils.prompts import SYSTEM_MESSAGE, USER_MESSAGE

chat = GigaChat(credentials=settings.gigachat_credentials)


async def generate(question: str, information: str) -> str:
    messages = [
        SystemMessage(content=SYSTEM_MESSAGE),
        HumanMessage(
            content=USER_MESSAGE.format(question=question, information=information)
        ),
    ]
    
    return await chat.agenerate(messages)
