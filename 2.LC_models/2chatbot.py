from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
print("Loaded token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))


model = ChatHuggingFace(llm=llm)
model.invoke("What is the capital of Pakistan?")  # Example usage