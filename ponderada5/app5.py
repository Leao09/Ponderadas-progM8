import os
from functools import partial
import openai
from dotenv import load_dotenv
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from PyPDF2 import PdfReader

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def preprocess_pdf(pdf_content):
    with open("temp.pdf", "wb") as f:
        f.write(pdf_content)
    pdf_reader = PdfReader("temp.pdf")
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ''
    return text

def manda_questao(question: str) -> dict:
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Você é um engenheiro de segurança do trabalho."},
                  {"role": "user", "content": question[4000]}]
    )

def recebe_ia_resposta(response: dict) -> str:
    return response["choices"][0]["message"]["content"]

def get_info(question: str, res: str) -> str:
    resp = manda_questao(f"{question}\n\n{res}")
    return recebe_ia_resposta(resp)

recebe_explicacao = partial(
    get_info,
    question="Explique sobre esta regra de segurança de maneira sucinta e em apenas 1 parágrafo, sem contextualizar"
)

def display_header() -> None:
    st.title("Bem-vindo ao Leão chat")
    st.text("Faça uma pergunta para o especialista em normas de seguranças industriais")

def display_widgets() -> tuple[UploadedFile, str]:
    uploaded_file = st.file_uploader("Faça upload de um arquivo PDF", type=["pdf"])
    text = st.text_area("Digite sua pergunta aqui")
    return uploaded_file, text

def estrai_resposta() -> tuple[UploadedFile, str]:
    uploaded_file, text = display_widgets()

    if uploaded_file:
        pdf_content = uploaded_file.read()
        text += preprocess_pdf(pdf_content)

    return uploaded_file, text

def main() -> None:
    display_header()

    uploaded_file, conteudo = estrai_resposta()

    if conteudo:
        with st.spinner(text="Humm...Estou pensando"):
            explanation = recebe_explicacao(res=conteudo)

        with st.spinner(text="Deixe-me pensar em uma resposta"):
            st.success("Nossa, essa foi difícil, mas aqui está sua resposta")
            st.write(explanation)

if __name__ == "__main__":
    main()