from database

import re 

banco_dados_paciente = []

def verificar_existência(bd, telefone): 
    
    for cadastro in bd:
        if cadastro["telefone"] == telefone:
            return True 
        else:
            return False 

def cadastrar(): 

    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente no formato 9xxxxxxxx: ") 

    padrao = r'^9\d{8}$'

    if nome == "": 
        return "Por gentileza, digite o seu nome!"
    elif telefone == "": 
        return "Por gentileza, digite o seu número de telefone! "
    elif not re.match(padrao, telefone):
        return "Por gentileza, digite o seu número de telefone no formato correto!"
    elif not 

def show_menu():
    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar')
        print('2. Opção 2')
        print('3. Opção 3')
        print('4. Sair')
        
        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            retorno = cadastrar()
            print(retorno)
        elif choice == '2':
            # print('Você escolheu a Opção 2')
            print(banco_dados_paciente)
        elif choice == '3':
            print('Você escolheu a Opção 3')
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

show_menu()