# To build application
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_core.output_parsers import StrOutputParser
import uvicorn
import os
from langchain_community.llms import Ollama 
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

app= FastAPI(
    title= "Langchain",
    version= "1.0",
    description="A simplr API Server"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"
# )
# model= ChatOpenAI()
##ollama llama2
llm= Ollama(model= "llama3.2")

prompt1= ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2= ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

# add_routes(
#     app,
#      prompt1|model,
#      path="/eassy"
# )

add_routes(
    app,
     prompt2|llm,
     path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host= "localhost", port= 8000)