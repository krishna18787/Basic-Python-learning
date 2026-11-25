# maxwell-model/Maxwell-V1-Flash

import os

from dotenv import load_dotenv
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="nvidia/Qwen3.5-4B-Qwen3.8-27B-Draft",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    task="text-generation"
)

model = ChatHuggingFace(
    llm=llm
)

prompt = "What is the capital of India?"
response = model.invoke(prompt)

print(response.content)
