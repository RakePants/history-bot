from src.database.repositories import InformationRepository
from src.utils.embedder import embed

import logging


async def retrieve(question: str) -> str:
    embedded_question = await embed(question)

    result = await InformationRepository().query(embedded_question, top_k=3)

    seen = set()
    information = []

    logging.info(result)
    
    for d in result["matches"]:
        logging.info(d["id"])
        if d["score"] > 0.3:
            if d["metadata"]["text"] not in seen:
                information.append(
                    {
                        "source": d["metadata"]["document_name"],
                        "text": d["metadata"]["text"],
                    }
                )
                seen.add(d["metadata"]["text"])

    return str(information)
