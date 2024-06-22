import csv

#CRUD paciente 

def create_paciente(paciente, filename='pacientes.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=paciente.keys())
        writer.writerow(paciente)

def read_pacientes(filename='pacientes.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def get_paciente_by_telefone(telefone, filename='pacientes.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['telefone'] == telefone:
                return row
    return None
    
def update_paciente(target_telefone, new_data, filename='pacientes.csv'):
    updated = False
    rows = read_pacientes(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=new_data.keys())
        writer.writeheader()
        for row in rows:
            if row['telefone'] == target_telefone:
                writer.writerow(new_data)
                updated = True
            else:
                writer.writerow(row)
    return updated

def delete_paciente(target_telefone, filename='pacientes.csv'):
    deleted = False
    rows = read_pacientes(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            if row['telefone'] != target_telefone:
                writer.writerow(row)
            else:
                deleted = True
    return deleted

#CRUD consulta 

def create_consulta(consulta, filename='consultas.csv'):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=consulta.keys())
        writer.writerow(consulta)

def read_consultas(filename='consultas.csv'):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def update_consulta(target_telefone, target_data, target_hora, new_data, filename='consultas.csv'):
    updated = False
    rows = read_consultas(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=new_data.keys())
        writer.writeheader()
        for row in rows:
            if row['telefone'] == target_telefone and row['data'] == target_data and row['hora'] == target_hora:
                writer.writerow(new_data)
                updated = True
            else:
                writer.writerow(row)
    return updated

def delete_consulta(target_telefone, target_data, target_hora, filename='consultas.csv'):
    deleted = False
    rows = read_consultas(filename)
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        for row in rows:
            if not (row['telefone'] == target_telefone and row['data'] == target_data and row['hora'] == target_hora):
                writer.writerow(row)
            else:
                deleted = True
    return deleted