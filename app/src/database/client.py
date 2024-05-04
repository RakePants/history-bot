from pinecone.grpc import PineconeGRPC

from src.config import settings

pc = PineconeGRPC(api_key=settings.pinecone_api_key)
index = pc.Index(host=settings.pinecone_host)
