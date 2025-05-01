from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import login
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic  import BaseModel, Field

# load_dotenv()
login(token="Your_hf_token")
llm=  HuggingFaceEndpoint(
    repo_id= "google/gemma-2-2b-it",
    task= "text-generation"
)

model= ChatHuggingFace(lm= llm)

class Person(BaseModel):
    
    name: str = Field(description= "Name of the person")
    age: int = Field(gt= 18, description= "Age of the person")
    city: str = Field(description= "Name of the city person belongs to")
    
parser= PydanticOutputParser(pydantic_object= Person)

template= PromptTemplate(
    template= 'Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables= ['place'],
    partial_variables={'format_instruction': parser.get_formate_instructions()} 
)

prompt= template.invoke({'place':'indian'})
# print(prompt)  #through which we can understand that what prompt we are sending to our LLM.

result= model.invoke(prompt)

final_result= parser.parse(result.content)

print(final_result)




# Through Chain

chain= template | model | parser

result= chain.invoke({'place':'indian'})

print(result)