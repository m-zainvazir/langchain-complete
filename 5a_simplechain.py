from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()