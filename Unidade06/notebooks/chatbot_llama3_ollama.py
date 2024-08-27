import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

if 'history' not in st.session_state:
    st.session_state.history = []

st.title("💬 Chatbot com LLM Local")
input_text = st.text_input("Qual a sua dúvida?", key='widget')

prompt = ChatPromptTemplate.from_messages([
        ("system", "Responda as perguntas em português do Brasil. Dê respostas curtas. Responda de forma técnica e não invente nada."),
        ("user", "question: {question}")
    ])

llm = Ollama(model="llama3")
output_parser = StrOutputParser()   
chain = prompt | llm | output_parser

response = chain.invoke({'question': input_text})
st.session_state.history.append({"question": input_text, "answer": response})

for chat in st.session_state.history:
    st.write(f"**Você**: {chat['question']}")
    st.write(f"**Chatbot**: {chat['answer']}")

