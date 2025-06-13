from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize ChatOpenAI with tracing enabled
llm = ChatOpenAI()
response = llm.invoke("Hello, world!")


