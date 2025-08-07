from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

parser = StrOutputParser()

prompt2= PromptTemplate(
    template="Explain the following joke {text}",
    input_variables=["text"]
)

chain = RunnableSequence(prompt1, model, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))