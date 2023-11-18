#! /bin/env python3
import re
import rclpy


intent_dict = {
    "sim": [r"\b(?:[Ss]im)"],
    "navegar_para": [
        r"\b(?:[Vv][aá])\s(?:para)\s*(?:[oa])?\s\b (.+)$",
        r"\b(?:[Vv][aá]|[Ii]r)?[ ]*(?:[Pp]ara)?\b (.+)$",
        r"\b\s*va\s*para\s\b (.+)",
        r"\b(?:[Aa]nde|[Nn]avegue|[Ss]e\s*locomova)\s*para\b[ ]*(.+)$",
        r"\b(?:[Aa]nde|[Nn]avegue|[Ss]e\s*[lL]ocomova)\s*[Pp]ara\b[ ]*(.+)$"
        r"\b(?:[Aa]nde|[Cc]aminhe|[Nn]avegue|[Ss]e\s*locomova)\s*para\b[ ]*(.+)$"
        r"\b\s*(?:[Aa]nde|[Nn]avegue|[Ss]e\s*locomova)\s*para\b\s*(.+)$"
    ],
    "nao": [r"\b[Nn][aã]o"]
}

action_dict = {
    "navegar_para": lambda nav: f"Navegando para {nav}",
    "sim": lambda _: True,
    "nao": lambda _: False
}


def nav_prompt(command):
    for key, patterns in intent_dict.items():
        for pattern in patterns:
            match = re.match(pattern, command, re.IGNORECASE)
            if match is not None:
                result = action_dict[key](match.group(len(match.groups())))
                return result

    return "Desculpe, não entendi o seu comando"

def main():
    rclpy.init()
    continua = True
    while (continua):
        command = input("Para onde você deseja ir?")
        resposta = nav_prompt(command)
        print(resposta)
        resposta2 = input("deseja continuar com essa conversa?")
        continua = bool(nav_prompt(resposta2))
    rclpy.shutdown()

if __name__ == '__main__':
    main()

