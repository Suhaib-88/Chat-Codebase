import streamlit as st
from streamlit_chat import message
from src.retriever import create_code_retriever
from src.coder import create_codebase
from src.constants import *

st.session_state.clicked = True

@st.cache_resource(show_spinner=True)
def create_code_pipeline():
    print("Creating code retriever and codebase bot...")  # Debug print statement
    code_retriever = create_code_retriever()
    print("Code retriever created.")  # Debug print statement
    codebase_bot = create_codebase()
    print("Codebase bot created.")  # Debug print statement

    return code_retriever, codebase_bot

code_retriever, codebase_bot = create_code_pipeline()

def display_conversation(history):
    print("Displaying conversation history...")  # Debug print statement
    for i in range(len(history['assistant'])):
        print(f"User: {history['user'][i]}, Assistant: {history['assistant'][i]}")  # Debug print statement
        message(history['user'][i], is_user=True, key=str(i) + "_user")
        message(history['assistant'][i], key=str(i))

if st.session_state.clicked:
    st.title('Coding bot')
    st.subheader('AI coding partner')
    
    print("Setting up session state...")  # Debug print statement
    if "assistant" not in st.session_state:
        st.session_state['assistant'] = ['Hi, how are you']

    if "user" not in st.session_state:
        st.session_state['user'] = ['Hey']

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('coder.jpg')

    with col2:
        with st.expander("Ask code"):
            code_query_inp = st.text_input("Query")
            if st.button("Send"):
                print(f"User query: {code_query_inp}")  # Debug print statement
                docs = code_retriever.get_relevant_documents(code_query_inp)
                print(f"Retrieved documents: {docs}")  # Debug print statement
                st.session_state["user"].append(code_query_inp)
                assistant_response = codebase_bot({
                    'input_documents': docs,
                    "question": code_query_inp
                }, return_only_outputs=True)['output_text']
                print(f"Assistant response: {assistant_response}")  # Debug print statement
                st.session_state["assistant"].append(assistant_response)

                if st.session_state["assistant"]:
                    display_conversation(st.session_state)

