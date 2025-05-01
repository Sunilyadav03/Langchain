from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm= ChatAnthropic(model= "", temperature= 0.2)
result= llm.invoke("what is the capital of russia?")
print(result.content)