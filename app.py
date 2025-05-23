from Agent.graph import get_graph
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import streamlit as st

Agent = get_graph()


st.title("Vitteey Sahaayak")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

if prompt:
    messages = [HumanMessage(content=prompt)]
    result = Agent.stream({"messages": messages}, stream_mode='values')
    for _ in result:
        i = _['messages'][-1]
        if isinstance(i, AIMessage) and i.content:
            response = i.content
            with st.chat_message("assistant"):
                st.markdown(response)
    
            st.session_state.messages.append({"role": "assistant", "content": response})

        i.pretty_print()











