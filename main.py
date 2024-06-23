from funcionalidades.cadastroPaciente import cadastrarPaciente
from funcionalidades.cadastroConsulta import cadastrarConsulta
from funcionalidades.cancelar_remarcar_consulta import cancelar_consulta
from utils.funcoes_uteis import RED, GREEN, YELLOW, BLUE, RESET
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    while True:
        clear_screen()
        
        print("="*50)
        print("CLÍNICA ÁGIL".center(50))
        print("="*50)
        print("")
        print("Olá! Seja bem-vindo(a) à Clínica Ágil!")
        print("Eu me chamo Lucy e serei a sua assistente virtual ;)")
        print("")
        print("Saiba que nós da Clínica Ágil estamos há mais de 20 anos")
        print("cuidando da saúde das famílias brasileiras.")
        print("")
        print("Estamos na rua Alameda Sempre Verde, número 188,")
        print("próximo ao shopping Seja Feliz.")
        print("")
        print("Contatos:")
        print("Telefone: (99) 99999-9999")
        print("Email: clinicaagilidade@email.com")
        print("")
        print("="*50)
        print("Sem mais delongas, vamos lá!!")
        print("")
        print("Escolha uma opção:")
        print("1. Cadastrar paciente")
        print("2. Marcar consulta")
        print("3. Cancelar/Remarcar consulta")
        print("4. Sair")
        print("="*50)
        
        choice = input(f"{YELLOW}Digite o número da opção desejada:{RESET} ")
        print()

        if choice == '1':
            cadastrarPaciente()
        elif choice == '2':
            cadastrarConsulta()
        elif choice == '3':
            cancelar_consulta()
        elif choice == '4':
            print(f"{YELLOW}Agradecemos a preferência! Volte sempre!!{RESET}")
            break
        else:
            print(f"{RED}Opção inválida. Tente novamente.{RESET}")
            input(f"{YELLOW}Pressione Enter para continuar...{RESET}")

show_menu()
