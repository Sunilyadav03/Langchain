from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import login
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# load_dotenv()
login(token="your_hf_token")
llm=  HuggingFaceEndpoint(
    repo_id= "google/gemma-2-2b-it",
    task= "text-generation"
)

model= ChatHuggingFace(lm= llm)
parser= StructuredOutputParser()

schema= [
    ResponseSchema(name= "fact_1", description='Fact 1 about the topic'),
    ResponseSchema(name= "fact_2", description='Fact 2 about the topic'),
    ResponseSchema(name= "fact_3", description='Fact 3 about the topic'),
]

template= PromptTemplate(
    template= "Give 3 facts about the {topic} \n {format_instruction}",
    input_variables= ['topic'],
    partial_variables={'format_instruction': parser.get_formate_instructions()}
)

prompt= template.invoke({'topic': 'black hole'})

result= model.invoke(prompt)

final_result= parser.parse(result.content)

print(final_result)




# With chaining (after "template")
chain= template | model | parser

result= chain.invoke({'topic': 'black hole'})

print(result)  