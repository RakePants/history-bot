import logging

from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI as ChatAPI

from src.config import settings
from src.utils.prompts import SYSTEM_MESSAGE, USER_MESSAGE

custom_llm = ChatAPI(
    base_url=settings.llm_url + "/v1",
    api_key="sk-not-required",
    verbose=False,
    temperature=0,
    model="lightblue/suzume-llama-3-8B-multilingual",
    extra_body={"stop_token_ids": [128009]},
)


async def generate(question: str, information: str) -> str:
    messages = [
        SystemMessage(content=SYSTEM_MESSAGE),
        HumanMessage(
            content=USER_MESSAGE.format(question=question, information=information)
        ),
    ]

    res = await custom_llm.agenerate(messages=[messages])
    logging.info(res)
    
    return res.generations[0][0].text
