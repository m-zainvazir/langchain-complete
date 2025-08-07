from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a 5 pointer summary on the following text: {text}",
    input_variables=["text"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Unemployment in Pakistan'})

print(result)