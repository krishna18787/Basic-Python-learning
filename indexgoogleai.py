import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

prompt = "What is the capital of India?"
response = model.invoke([HumanMessage(content=prompt)])

content = response.content
if isinstance(content, list):
    print("".join(part.get("text", "") for part in content if isinstance(part, dict)))
else:
    print(content)