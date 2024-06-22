from database.database import read_pacientes, create_consulta, ler_consultas_por_data
from funcionalidades.cadastroPaciente import cadastrarPaciente
from funcionalidades.cadastroConsulta import cadastrarConsulta
from datetime import datetime

# banco_dados_paciente = []

# def verificar_existência(bd, telefone): 
    
#     for cadastro in bd:
#         if cadastro["telefone"] == telefone:
#             return True 
#         else:
#             return False 
    


def show_menu():
    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar paciente')
        print('2. Marcar consulta')
        print('3. Opção 3')
        print('4. Sair')
        
        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            retorno = cadastrarPaciente()
            print(retorno)
        elif choice == '2':
            # print('Você escolheu a Opção 2')
            cadastrarConsulta()
        elif choice == '3':
            # print('Você escolheu a Opção 3')
            print(read_pacientes())
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

show_menu()