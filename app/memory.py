import redis, json
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

vector_store = Chroma(
    collection_name="travel_memory",
    embedding_function=OpenAIEmbeddings()
)
