import os
import types
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, Graph

# Load environment from .env file
load_dotenv()




llm_big = ChatGroq(model="llama3-8b-8192",api_key=os.environ.get('GROQ_API_KEY'))
llm_small = ChatGroq(mode="llama2", api_key=os.environ.get('GROQ_API_KEY'))

