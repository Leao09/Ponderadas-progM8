import os
from functools import partial
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def manda_questao(question:str)-> dict:
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system","content":"Você é um engenheiro de segurança do trabalho."},
                  {"role":"user","content":question}]
    )

def recebe_ia_resposta(response:dict)->str:
    return response["choices"][0]["message"]["content"]

def get_info(question:str,res:str)->str:
    resp = manda_questao(f"{question}\n\n{res}")
    return recebe_ia_resposta(resp)


recebe_explicacao = partial(
    get_info,
    question = "Explique sobre está regra de segurança de maneira sucinta e em apenas 1 parágrafo, sem contextualizar"
)