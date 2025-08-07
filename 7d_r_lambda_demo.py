from langchain.schema.runnable import RunnableLambda

def word_counter(text):
    return len(text.split())

runnable_word_counter = RunnableLambda(word_counter)

print(runnable_word_counter.invoke("This is a test sentence."))  # Output: 5