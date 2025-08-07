from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a Linkendin post about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkendin": RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({"topic": "AI"})

print(result['tweet'])
print(result['linkendin'])