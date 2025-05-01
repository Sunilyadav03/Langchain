from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_core.prompts import PromptTemplate

# load_dotenv()

model= ChatOpenAI()

#Problem- query-->LLM-->detailed_report_on_query_report-->LLM--->summary_of_that detailed_report

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





# With 'StrOutputParser'





from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

model= ChatOpenAI()

#Problem- query-->LLM-->detailed_report_on_query_report-->LLM--->summary_of_that detailed_report

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

parser= StrOutputParser()

chain= template1 | model | parser | template2 | model | parser

result= chain.invoke({'topic':'black hole'})

print(result)
