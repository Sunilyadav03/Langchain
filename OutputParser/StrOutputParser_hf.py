from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_core.prompts import PromptTemplate

# load_dotenv()
login(token="Your_hf_token")
llm=  HuggingFaceEndpoint(
    repo_id= "google/gemma-2-2b-it",
    task= "text-generation"
)

model= ChatHuggingFace(llm= llm )

#Parser Use case:- query-->LLM-->detailed_report_on_query_report-->LLM--->summary_of_that detailed_report

#1st Template----> Detailed Report
template1= PromptTemplate(
    template= 'write a detailed report on {topic}',
    input_variables=['topic']
)


# 2nd Template---> Summary
template2= PromptTemplate(
    template= 'write a 5 line summary on the following text./n {text}',
    input_variables=['text']
)

prompt1= template1.invoke({'topic':'black hole'})
result= model.invoke(prompt1)

prompt2= template2.invoke({'text': result.content})
f_res= model.invoke(prompt2)

print(f_res.content)

