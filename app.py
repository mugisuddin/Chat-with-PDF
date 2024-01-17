import streamlit as st
from PyPDF2 import PdfReader 
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, Document
import os 
import openai
from dotenv import load_dotenv
load_dotenv()

st.header("Talk with PDF!")

def process_pdf(pdf):
    file = PdfReader(pdf)
    text = ""
    for page in file.pages:
        text += str(page.extract_text())
    return text


uploaded_pdf = st.file_uploader("Upload your own pdf!")

if uploaded_pdf is not None:
    st.write("Your pdf is being processed...")
    # Processing and uploading pdf to llama-index index
    extract_text_from_pdf = process_pdf(uploaded_pdf)

    doc = Document(text=extract_text_from_pdf)

    index = VectorStoreIndex([]) 

    index.insert(doc)

    # Question answering with pdf

    user_question = st.text_input("Enter your question: ")

    if user_question is not None: 

        chat_engine = index.as_chat_engine()

        response = chat_engine.chat(user_question)

        st.write(response.response)
        print(response.response)









