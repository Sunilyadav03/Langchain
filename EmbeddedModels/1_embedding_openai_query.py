from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model= "text-embedding-3-large", dimensions= 32)   #High dimension leads to the high model cost. But in other hand, if dimension is high then model will capture more accurate context meaning. 

result= embedding.embed_query("New delhi is the capital of India.")   #embed_query:- is used to generate embedding of the single query.

print(str(result))


