from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model= ChatOpenAI()

#Schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model= model.with_structured_output(Review)

result= structured_model.invoke("""The hardware is great, but the software feels bloated. there are too many 
                                pre-installed apps that i can't remove. also, The UI looks outdated compare to other
                                brands. Hoping for a software update to fix this.""")

print(result)
print(result["summary"])
print(result["sentiment"])
