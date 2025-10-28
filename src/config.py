import os
from dotenv import load_dotenv

load_dotenv()
VECTOR_DB_KEY=os.getenv("PINECONE_API_KEY")
VECTOR_DB_HOST=os.getenv("VECTOR_DB_HOST")