from datetime import datetime
from database.database import ler_consultas_por_data

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def validar_data(data):
    try:
        data_valida = datetime.strptime(data, "%d/%m/%y")
        return data_valida
    except ValueError:
        return None

# Função para validar o horário
def validar_horario(horario):
    try:
        hora_int = int(horario)
        if 8 <= hora_int <= 20:
            return True
        else:
            return False
    except ValueError:
        return False
    
def selecao_pacientes(pacientesCadastrados):
        for i, paciente in enumerate(pacientesCadastrados):
            print(f"{BLUE}{i} - {paciente['nome']}{RESET}")
        print(f"{BLUE}{len(pacientesCadastrados) + 1} - Voltar para o menu principal{RESET}")

        numPacienteEscolhido = int(input(f"{YELLOW}Por favor, escolha um número correspondente a um paciente:{RESET}"))
    
        if numPacienteEscolhido > (len(pacientesCadastrados) + 1) or numPacienteEscolhido <= 0:
            print(f"{RED}O número digitado não está relacionado a nenhum paciente.{RESET}")
            input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
            return 
        
        if numPacienteEscolhido == len(pacientesCadastrados) + 1:
            return None 
        else: 
            pacienteEscolhido = pacientesCadastrados[numPacienteEscolhido - 1]

        return pacienteEscolhido

def selecao_data(): 
    data = input(f"{YELLOW}Por favor, digite a data da consulta no formato dd/mm/yy:{RESET} ")

    data_valida = validar_data(data)
    if not validar_data(data):
        print(f"{YELLOW}Por favor, digite a data no formato dd/mm/yy.{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return None 

    # Verifica se a data do agendamento não é anterior ao dia atual
    if data_valida.date() < datetime.now().date():
        print(f"{RED}A data do agendamento não pode ser anterior ao dia atual.{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return None 
    
    return data 

def selecao_horario(data): 

    horarios_disponíveis = ler_consultas_por_data(data)

    if len(horarios_disponíveis) == 0: 
        print(f"{YELLOW}Desculpe! Mas não temos nenhum horários disponível para esse dia :(){RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return None 

    for i, j in enumerate(horarios_disponíveis):
        print(f"{BLUE}{i + 1} - {j}{RESET}")
    print(f"{BLUE}{len(horarios_disponíveis) + 1} - Voltar para o menu principal{RESET}")

    hora = int(input(f"{YELLOW}Por favor, digite o número relacionado a um horário para a consulta:{RESET} "))

    if hora == len(horarios_disponíveis) + 1:
        return None 

    if not validar_horario(hora + 7):
        print(f"{RED}Por favor, digite um horário válido.{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...")
        return None 
    
    return hora 

def selecao_especialidade(): 

    especialidades = [
        "Cardiologia", "Dermatologia", "Endocrinologia", "Gastroenterologia",
        "Geriatria", "Ginecologia", "Hematologia", "Infectologia",
        "Nefrologia", "Neurologia", "Oftalmologia", "Ortopedia",
        "Otorrinolaringologia", "Pediatria", "Psiquiatria", "Reumatologia", "Urologia"
    ]

    for i, especialidade in enumerate(especialidades, start=1):
        print(f"{BLUE}{i} - {especialidade}{RESET}")
    print(f"{BLUE}18 - Voltar para o menu principal{RESET}")

    escolhaEspecialidade = int(input(f"{YELLOW}Por favor, digite o número relacionado a uma de nossas especialidades:{RESET} "))

    if escolhaEspecialidade == 18:
        return None 

    if escolhaEspecialidade < 1 or escolhaEspecialidade > len(especialidades):
        print(f"{RED}Escolha inválida.{RESET}")
        input(f"{YELLOW}Pressione Enter para continuar...{RESET}")
        return None 

    especialidadeEscolhida = especialidades[escolhaEspecialidade - 1]

    return especialidadeEscolhida