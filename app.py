import streamlit as st
from dotenv import load_dotenv
import os

from graph import build_graph


load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "AI-Diagnosa-Komputer"


st.set_page_config(
    page_title="AI Diagnosa Komputer",
    layout="wide"
)

st.title(" AI Diagnosa Komputer ")


app = build_graph()


if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header("⚙️ Menu")
    if st.button("🗑️ Reset Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.info("")


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ketik gejala komputer...")

if user_input:

    
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    
    chat_history = "\n".join(
        [f"{m['role']}: {m['content']}" for m in st.session_state.messages]
    )


    with st.chat_message("assistant"):
        with st.spinner("AI sedang menganalisis... 🤖"):

            result = app.invoke({
                "input": user_input,
                "history": chat_history
            })

            ai_response = result["output"]

            st.markdown(ai_response)

    
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })