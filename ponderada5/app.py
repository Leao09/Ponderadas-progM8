import io
import os
import openai
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader

load_dotenv()
openai.api_key =  os.getenv('OPENAI_API_KEY')

def preprocess_pdf():
    loader = PyPDFLoader("Workshop rules and safety considerations _ Students.pdf")
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    
    vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())

    retriever = vectorstore.as_retriever()

    return retriever

def generate_openai_response(message: str, retriever) -> str:
    template = """Answer the question based only on the following context:
    {context}
    
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    model = ChatOpenAI(model="gpt-3.5-turbo")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
    )
    response = ""
    for s in chain.stream(message):
        print(s.content, end="", flush=True)
        response += s.content
    return response



def main():
    retriever = preprocess_pdf()
    
    st.title("Bem vindo ao Leao-chat")


    question = str(st.text_input("Digite sua pergunta aqui"))

    if st.button("Enviar pergunta"):
        with st.spinner("Aguarde, estamos gerando uma resposta..."):
            answer = generate_openai_response(question, retriever)
            st.success(f"Resposta: {answer}")

if __name__ == "__main__":
    main()