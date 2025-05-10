import os

import streamlit as st


from langchain_groq import ChatGroq

from langchain_core.prompts import (
                                        SystemMessagePromptTemplate,
                                        HumanMessagePromptTemplate,
                                        ChatPromptTemplate,
                                        MessagesPlaceholder
                                        )


from langchain_core.runnables.history import RunnableWithMessageHistory
from sqlalchemy import create_engine
from langchain_community.chat_message_histories import SQLChatMessageHistory

from langchain_core.output_parsers import StrOutputParser

api_key=os.getenv('API_KEY')

st.set_page_config(
    page_title="AI Chat Companion",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("🤖 AI Chat Companion")
st.markdown("---")


# Create SQLAlchemy engine
engine = create_engine("sqlite:///chat_history-custom.db")
def get_session_history(session_id: str) -> SQLChatMessageHistory:
    return SQLChatMessageHistory(
        session_id=session_id,
        connection=engine
    )
# Custom CSS styling
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2e2e2e 0%, #1a1a1a 100%);
        color: white;
    }
    .sidebar-title {
        font-size: 1.5em;
        color: #4CAF50;
        margin-bottom: 20px;
    }
    .chat-bubble {
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        max-width: 80%;
    }
    .user-bubble {
        background-color: #4CAF50;
        color: white;
        margin-left: auto;
    }
    .bot-bubble {
        background-color: #333333;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown('<p class="sidebar-title">Chat Settings</p>', unsafe_allow_html=True)

    user_id = st.text_input("Your User ID", "USER", help="Enter a unique identifier for your chat session")

    st.markdown("---")
    if st.button("🧹 Starting New Conversation", use_container_width=True):
        st.session_state.chat_history = []
        history = get_session_history(user_id)
        history.clear()
        st.rerun()

    st.markdown("---")
    with st.expander("Model Configuration"):
        model = st.selectbox(
            "AI Model",
            ["meta-llama/llama-4-maverick-17b-128e-instruct",'deepseek-r1-distill-llama-70b'],
            index=0,
            help="Select the AI model to use for conversation"
        )
        temperature = st.slider(
            "Creativity Level",
            min_value=0.0,
            max_value=1.0,
            value=0.6,
            help="Control the model's creativity (lower = more factual, higher = more creative)"
        )

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages
for message in st.session_state.chat_history:
    avatar = "👤" if message['role'] == 'user' else "🤖"
    with st.chat_message(message['role'], avatar=avatar):
        st.markdown(f"<div class='chat-bubble {'user-bubble' if message['role'] == 'user' else 'bot-bubble'}'>"
                    f"{message['content']}"
                    f"</div>", unsafe_allow_html=True)





llm = ChatGroq(model=model, temperature=temperature, api_key=api_key)

system = SystemMessagePromptTemplate.from_template(
    "You are an insightful and helpful assistant. Provide concise, organized responses with markdown formatting when appropriate.")
human = HumanMessagePromptTemplate.from_template("{input}")

messages = [system, MessagesPlaceholder(variable_name='history'), human]
prompt = ChatPromptTemplate(messages=messages)
chain = prompt | llm | StrOutputParser()

runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='input',
    history_messages_key='history'
)


def chat_with_llm(session_id, input):
    for output in runnable_with_history.stream(
            {'input': input},
            config={'configurable': {'session_id': session_id}}
    ):
        yield output


# Chat input
prompt = st.chat_input("Type your message here...", key="chat_input")

# User input handling
if prompt:
    st.session_state.chat_history.append({'role': 'user', 'content': prompt})

    with st.chat_message("user", avatar="👤"):
        st.markdown(f"<div class='chat-bubble user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant", avatar="🤖"):
        response = st.write_stream(chat_with_llm(user_id, prompt))
        st.session_state.chat_history.append({'role': 'assistant', 'content': response})

# Add footer
st.markdown("""
---
**Powered by AmirHossein**  
![Groq](https://groq.com)  
*Lightning-fast AI responses*
""")

