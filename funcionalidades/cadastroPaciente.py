from database.database import create_paciente, get_paciente_by_telefone
import re

def cadastrarPaciente(): 
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente no formato 9xxxxxxxx: ") 

    padrao = r'^9\d{8}$'

    if nome == "": 
        print("Por gentileza, digite o seu nome!")
        return
    elif telefone == "": 
        print("Por gentileza, digite o seu número de telefone!")
        return
    elif not re.match(padrao, telefone):
        print("Por gentileza, digite o seu número de telefone no formato correto!")
        return
    elif get_paciente_by_telefone(telefone) is None: 
        paciente = {
            'nome': nome, 
            'telefone': telefone
        }

        create_paciente(paciente)
        print("Paciente cadastrado com sucesso")
        return
    else: 
        print("Paciente já cadastrado!")
        return
