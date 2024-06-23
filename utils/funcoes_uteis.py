from datetime import datetime
from database.database import ler_consultas_por_data

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
        for i, paciente in enumerate(pacientesCadastrados, start=1):
            print(f"{i} - {paciente['nome']}")
        print(f"{len(pacientesCadastrados) + 1} - Voltar para o menu principal")

        numPacienteEscolhido = int(input("Por favor, scolha um número correspondente a um paciente: "))
    
        if numPacienteEscolhido > (len(pacientesCadastrados) + 1) or numPacienteEscolhido <= 0:
            print("O número digitado não está relacionado a nenhum paciente.")
            input("Pressione Enter para continuar...")
            return 
        
        if numPacienteEscolhido == len(pacientesCadastrados) + 1:
            return None 
        else: 
            pacienteEscolhido = pacientesCadastrados[numPacienteEscolhido - 1]

        return pacienteEscolhido

def selecao_data(): 
    data = input("Por favor, digite a data da consulta no formato dd/mm/yy: ")

    data_valida = validar_data(data)
    if not validar_data(data):
        print("Por favor, digite a data no formato dd/mm/yy.")
        input("Pressione Enter para continuar...")
        return None 

    # Verifica se a data do agendamento não é anterior ao dia atual
    if data_valida.date() < datetime.now().date():
        print("A data do agendamento não pode ser anterior ao dia atual.")
        input("Pressione Enter para continuar...")
        return None 
    
    return data 

def selecao_horario(data): 

    horarios_disponíveis = ler_consultas_por_data(data)

    if len(horarios_disponíveis) == 0: 
        print("Desculpe! Mas não temos nenhum horários disponível para esse dia :()")
        input("Pressione Enter para continuar...")
        return None 

    for i, j in enumerate(horarios_disponíveis):
        print(f"{i + 1} - {j}")
    print(f"{len(horarios_disponíveis) + 1} - Voltar para o menu principal")

    hora = int(input("Por favor, digite o número relacionado a um horário para a consulta: "))

    if hora == len(horarios_disponíveis) + 1:
        return None 

    if not validar_horario(hora + 7):
        print("Por favor, digite um horário válido.")
        input("Pressione Enter para continuar...")
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
        print(f"{i} - {especialidade}")
    print("18 - Voltar para o menu principal")

    escolhaEspecialidade = int(input("Por favor, digite o número relacionado a uma de nossas especialidades: "))

    if escolhaEspecialidade == 18:
        return None 

    if escolhaEspecialidade < 1 or escolhaEspecialidade > len(especialidades):
        print("Escolha inválida.")
        input("Pressione Enter para continuar...")
        return None 

    especialidadeEscolhida = especialidades[escolhaEspecialidade - 1]

    return especialidadeEscolhida