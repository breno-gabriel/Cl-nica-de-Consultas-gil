from database.database import create_paciente, get_paciente_by_telefone
from utils.funcoes_uteis import RED, GREEN, YELLOW, BLUE, RESET
import re

def cadastrarPaciente(): 
    nome = input(f"{YELLOW}Por favor, digite o seu nome:{RESET} ")

    padrao = r'^9\d{8}$'

    if nome.strip() == "": 
        print(f"{YELLOW}Por favor, digite o seu nome!{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return
    
    telefone = input(f"{YELLOW}Por favor, digite o seu telefone (formato 9xxxx-xxxx):{RESET} ") 

    if telefone.strip() == "": 
        print(f"{RED}Você não digitou o seu telefone!{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return
    elif not re.match(padrao, telefone):
        print(f"{RED}O número de telefone precisa estar no formato 9xxxx-xxxx.{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return
    
    if get_paciente_by_telefone(telefone) is None: 
        paciente = {
            'nome': nome, 
            'telefone': telefone
        }

        create_paciente(paciente)
        print()
        print(f"{GREEN}Paciente cadastrado com sucesso!{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
    else: 
        print()
        print(f"{RED}Paciente já cadastrado!{RESET}")
        input(f"{GREEN}Pressione Enter para continuar...{RESET}")
