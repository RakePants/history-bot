from src.utils.embedder import embed
from src.database.repositories import InformationRepository


def retrieve(question: str) -> str:
    embedded_question = embed(question)

    results = InformationRepository().query(embedded_question)

    seen = set()
    information = []

    for d in results:
        if d["metadata"]["parent_text"] not in seen:
            information.append(
                {
                    "source": d["metadata"]["document_name"],
                    "text": d["metadata"]["parent_text"],
                }
            )
            seen.add(d["metadata"]["parent_text"])

    return "\n\n".join(information)
