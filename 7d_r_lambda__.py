from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_counter(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

final_result = """{} \n wordcount: {}""".format(result['joke'], result['word_count'])

print(final_result)  # Output will include the joke and its word count