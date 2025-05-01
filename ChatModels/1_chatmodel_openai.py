from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, max_completion_tokens= 10)
result= llm.invoke("What is the capital of rajasthan")
# print(reult)
# print(result.content)
