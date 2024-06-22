from database.database import create_paciente, get_paciente_by_telefone

import re

def cadastrarPaciente(): 

    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente no formato 9xxxxxxxx: ") 

    padrao = r'^9\d{8}$'

    if nome == "": 
        return "Por gentileza, digite o seu nome!"
    elif telefone == "": 
        return "Por gentileza, digite o seu número de telefone!"
    elif not re.match(padrao, telefone):
        return "Por gentileza, digite o seu número de telefone no formato correto!"
    elif  get_paciente_by_telefone(telefone) is None: 

        paciente = {
            'nome': nome, 
            'telefone': telefone
        }

        create_paciente(paciente)

        return "Paciente cadastrado com sucesso"
    else: 
        return "Paciente já cadastrado!"