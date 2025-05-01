from langchain_huggingface import HuggingFaceEmbeddings

embedding= HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2") 

#for single Query:-
# text= "Delhi is the capital of India"

# vector= embedding.embed_query(text)
# print(str(vector))

#for docs:- 
documents= [
    "Delhi is capital of India",
    "Jaipur is the capital of Rajasthan",
    "shimla is the capital of Himachal Pradesh"
]

vector= embedding.embed_documents(documents)
print(str(vector))
