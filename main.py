from database.database import read_consultas, delete_consulta, update_consulta
from funcionalidades.cadastroPaciente import cadastrarPaciente, get_paciente_by_telefone
from funcionalidades.cadastroConsulta import cadastrarConsulta
from funcionalidades.cancelar_remarcar_consulta import cancelar_consulta
from datetime import datetime
from utils.funcoes_uteis import selecao_especialidade,selecao_data, selecao_horario


def show_menu():
    while True:
        print('\nEscolha uma opção:')
        print('1. Cadastrar paciente')
        print('2. Marcar consulta')
        print('3. Cancelar/Remarcar consulta')
        print('4. Sair')
        
        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            retorno = cadastrarPaciente()
            print(retorno)
        elif choice == '2':
            cadastrarConsulta()
        elif choice == '3':
            cancelar_consulta()
        elif choice == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

show_menu()