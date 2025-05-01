from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
 
model= ChatOpenAI()

parser1= StrOutputParser()

class Feedback(BaseModel):
    
    sentiment: Literal['positive', 'negative']= Field(description= "Give the sentiment of the feedback.")
    
parser2= PydanticOutputParser(pydantic_object= Feedback)
 


prompt1= PromptTemplate(
    template= "Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables= ['feedback'],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}
)


classifier_chain= prompt1 | model | parser2

# print(classifier_chain.invoke({'feedback': 'This is a wounderful smartphone'}).sentiment)  # This will return the sentiment of the input feedback.

prompt2= PromptTemplate(
    template= "Write an appropriate response to this positive feedback \n {feedback}",
    input_variables= ['feedback'],
)

prompt3= PromptTemplate(
    template= "Write an appropriate response to this negative feedback \n {feedback}",
    input_variables= ['feedback'],
)

#  In RunnableBranch we pass parameteres in the format of the tuple. and in the each tuple we pass two things:- 1. condition, 2. Chain (which will be executed when condition is True) and in the last we set a default chain which will be executed in case, when none of the above chains are not executed.so this is kind of (if-else, if-else, else)

branch_chain= RunnableBranch(
    # (condition1, chain1),
    # (condition2, chain2),
    # default chain
    
    (lambda x:x.sentiment== "positive", prompt2 | model | parser1),            # here x is  "sentiment= positive/negative"
    (lambda x:x.sentiment== "negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "Could not find any sentiment")
)  

chain= classifier_chain | branch_chain

final_result= chain.invoke({'feedback': "This is a terrible phone."})

print(final_result)


# Visualize the chain.

chain.get_graph().print_ascii()