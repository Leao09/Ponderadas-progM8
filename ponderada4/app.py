import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


from leaoChat import recebe_explicacao

def display_header()-> None:
    st.title("Bem vindo ao Leão chat")
    st.text("Faça uma pergunta para o especialista em normas de seguranças industriais")


def display_widgets() -> tuple[UploadedFile, str]:
    text = st.text_area("Digite sua pergunta aqui")
    return text


def estrai_resposta() -> str:
   resposta= display_widgets()

   return resposta or ""


def main() -> None:
    display_header()

    if conteudo := estrai_resposta():
        with st.spinner(text="Humm...Estou pensando"):
            explanation = recebe_explicacao(res=conteudo)

        with st.spinner(
            text=(
                "Deixe-me pensar em uma resposta"
            )
        ):

            st.success("Nossa essa foi dificil, mas aqui está sua resposta")
            st.write(explanation)


if __name__ == "__main__":
    main()