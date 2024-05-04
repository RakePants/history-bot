from src.database.repositories import InformationRepository
from src.utils.embedder import embed

import logging


async def retrieve(question: str) -> str:
    embedded_question = await embed(question)

    result = await InformationRepository().query(embedded_question)

    seen = set()
    information = []

    for d in result["matches"]:
        logging.info(d["id"])
        if d["metadata"]["parent_text"] not in seen:
            information.append(
                {
                    "source": d["metadata"]["document_name"],
                    "text": d["metadata"]["parent_text"],
                }
            )
            seen.add(d["metadata"]["parent_text"])

    return str(information)
