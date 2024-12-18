from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")    #used to store the outcomes and the results.


#Prompt Template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are my assistent. Please help me in my queries"),
        ("user", "Question:{question}")
    ]
    
)

##streamlit framework

st.title("Langchain Demo with OPENAI API")
input_txt= st.text_input("Search the topic which user want")

## OpenAI LLM

llm= ChatOpenAI(model= "gpt-3.5-turbo")
output_parser= StrOutputParser()

chain= prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'question': input_txt}))
    