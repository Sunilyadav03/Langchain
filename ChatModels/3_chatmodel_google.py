import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Step 1: Configure Gemini directly
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Step 2: Setup LangChain wrapper
llm = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Step 3: Invoke the model
response = llm.invoke("What is the capital of India?")
print(response.content)
