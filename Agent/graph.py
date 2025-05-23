from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from Agent.State import State
from Agent.tools import get_tools
from Agent.chatbot import get_chatbot

def get_graph():
    graph_builder= StateGraph(State)

    chatbot_node = get_chatbot()
    graph_builder.add_node("chatbot",chatbot_node)

    tools=get_tools()
    tool_node = ToolNode(tools=tools)
    graph_builder.add_node("tools", tool_node)

    graph_builder.add_edge(START,"chatbot")
    graph_builder.add_conditional_edges( "chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")


    graph=graph_builder.compile()
    return graph
    
    
    
