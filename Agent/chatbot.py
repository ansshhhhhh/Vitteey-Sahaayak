from langchain_groq import ChatGroq
from Agent.tools import get_tools
from Agent.State import State
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def get_chatbot():
    model="llama-3.1-8b-instant"
    llm=ChatGroq(groq_api_key=groq_api_key, model_name=model)
    tools=get_tools()
    llm_with_tools=llm.bind_tools(tools)
    def chatbot(state:State):
        return {"messages":[llm_with_tools.invoke(state["messages"])]}
    return chatbot




