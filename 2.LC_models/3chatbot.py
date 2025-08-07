from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ["HF_HOME"] = "C:/Projects/CampusX/GenAI/2.LC_models/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="mistralai/Magistral-Small-2506",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature= 0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
