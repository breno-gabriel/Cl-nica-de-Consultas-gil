from database.database import create_paciente, get_paciente_by_telefone
import re

def cadastrarPaciente(): 
    nome = input("Por favor, digite o seu nome: ")

    padrao = r'^9\d{8}$'

    if nome.strip() == "": 
        print("Por favor, digite o seu nome!")
        input("Pressione Enter para continuar...")
        return
    
    telefone = input("Por favor, digite o seu telefone (formato 9xxxx-xxxx): ") 

    if telefone.strip() == "": 
        print("Você não digitou o seu telefone!")
        input("Pressione Enter para continuar...")
        return
    elif not re.match(padrao, telefone):
        print("O número de telefone precisa estar no formato 9xxxx-xxxx.")
        input("Pressione Enter para continuar...")
        return
    
    if get_paciente_by_telefone(telefone) is None: 
        paciente = {
            'nome': nome, 
            'telefone': telefone
        }

        create_paciente(paciente)
        print()
        print("Paciente cadastrado com sucesso!")
        input("Pressione Enter para continuar...")
    else: 
        print()
        print("Paciente já cadastrado!")
        input("Pressione Enter para continuar...")
