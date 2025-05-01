from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model= "text-embedding-3-large", dimensions= 32)  

documents= [
    "Delhi is capital of India",
    "Jaipur is the capital of Rajasthan",
    "shimla is the capital of Himachal Pradesh"
]

result= embedding.embed_documents(documents)     # embed_documents:- is used to generate embedding vectors for more than one sentence/query.

print(str(result))