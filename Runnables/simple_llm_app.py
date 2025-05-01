from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize the LLM 

llm= OpenAI(model_name= 'gpt-3.5-turbo', temperature= 0.7)

# Create a Prompt Template
prompt= PromptTemplate(
    template= "Build an attractive and energetic blog on the following topic \n {topic}",
    input_variables= ['topic']
)

# Define the input 
topic= input("enter your topic name: ")

# Format the prompt manually using PromptTemplate
formatted_prompt= prompt.format(topic= topic)

# Call the LLM directly
blog_topic= llm.predict(formatted_prompt)

print("Generated blog title: ", blog_topic)
  