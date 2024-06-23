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
        print(f"{YELLOW}CLÍNICA ÁGIL".center(50) + RESET)
        print("="*50)
        print("")
        print(f"{YELLOW}Olá! Seja bem-vindo(a) à Clínica Ágil!{RESET}")
        print(f"{YELLOW}Eu me chamo Lucy e serei a sua assistente virtual ;){RESET}")
        print("")
        print(f"{YELLOW}Saiba que nós da Clínica Ágil estamos há mais de 20 anos{RESET}")
        print(f"{YELLOW}cuidando da saúde das famílias brasileiras.{RESET}")
        print("")
        print(f"{YELLOW}Estamos na rua Alameda Sempre Verde, número 188,{RESET}")
        print(f"{YELLOW}próximo ao shopping Seja Feliz.{RESET}")
        print("")
        print(f"{YELLOW}Contatos:{RESET}")
        print(f"{YELLOW}Telefone: (99) 99999-9999{RESET}")
        print(f"{YELLOW}Email: clinicaagilidade@email.com{RESET}")
        print("")
        print("="*50)
        print(f"{YELLOW}Sem mais delongas, vamos lá!!{RESET}")
        print("")
        print(f"{YELLOW}Escolha uma opção:{RESET}")
        print(f"{YELLOW}1. Cadastrar paciente{RESET}")
        print(f"{YELLOW}2. Marcar consulta{RESET}")
        print(f"{YELLOW}3. Cancelar/Remarcar consulta{RESET}")
        print(f"{YELLOW}4. Sair{RESET}")
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
