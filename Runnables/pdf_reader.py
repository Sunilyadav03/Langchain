from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader 
 
# Document Loading
loader= TextLoader("file_path.txt")
documents= loader.load()

# Splitting the document into smaller chunks
text_spliter= RecursiveCharacterTextSplitter(chunk_size= 500, chunk_overlap= 50)
docs= text_spliter.split_documents(documents)

#Convert text into embeddings & store in FAISS
vectorstore= FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retriever (fetches relevant documents)
retriever= vectorstore.as_retriever()

#Manually Retrieve Relevant Documents
query= "What are the key takeaways from this document?"
retrieved_docs= retriever.get_relevant_documents(query)

#Combine retrieved text into a single prompt
retrieved_text= '\n'.join([doc.page_content for doc in retrieved_docs])

# Initialize the LLM
llm= OpenAI(model_name= 'get-3.5-turbo', temperature= 0.7)

#Manually pass Retrieved text into LLM
prompt= f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer= llm.predict(prompt)

#Print the Answer
print("Answer: ", answer)
