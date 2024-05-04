import numpy
import torch
from sentence_transformers import SentenceTransformer

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

embedding_model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", device=device
)


def embed(sequence: str) -> numpy.ndarray:
    embedding = embedding_model.encode(sequence)
    return embedding
