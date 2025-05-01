# from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from langchain_huggingface import HuggingFaceEmbeddings
# import numpy as np
from dotenv import load_dotenv

load_dotenv()

# embedding= OpenAIEmbeddings(model= 'text-embedding-3-large', dimensions= 300)

embedding= HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2") 

document= [
    "Virat Kohli is an India Cricketer Known for his aggressive batting and leadership.",
    "MS dhoni is a former Indian Captain famous for his calm demeanor and finishing skills.",
    "Sachin tendulkar, also known as the 'god of cricket', holds many batting records.",
    "Rohit sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast Bowler known for his unorthodox action and yorkers"
]

query= "virat kohli"

doc_embeddings= embedding.embed_documents(document)
query_embeddings= embedding.embed_query(query)

# cosine_similarity will return similarity score of the query_embeddings with the each embedding vector of the doc_embeddings(in the document, there are five sentences so "doc_embeddings" will be a 5 vector 2D list), 
scores= cosine_similarity([query_embeddings], doc_embeddings)[0]   # Always remember that we need to pass 2D list in the cosine_similarity method, so bcz "doc_embeddings" is already in 2D format,  But "query_embeddings" is in the 1D format that's why we pass it in the list to make it in the 2D format. and it will return similarity_scores in the 2D format. So we need to convert them into 1D then we used [0]
index, score= sorted(list(enumerate(scores)), key= lambda x: x[1])[-1]

print(scores)
print(query)
print(document[index])
print("Similarity score:", score)

