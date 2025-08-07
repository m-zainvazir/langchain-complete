from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

loader= TextLoader("Data Science.txt")

docs = loader.load()

print(type(docs))

print(len(docs))

#print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"text": docs[0].page_content}))