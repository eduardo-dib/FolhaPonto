#Importando as bibliotecas
import random
from datetime import datetime, timedelta
#Input do usuário para definir quantos dias ele trabalhou
#diasTrabalhados = int(input("Quantos dias você trabalhou? "))
#if(diasTrabalhados < 1 or diasTrabalhados > 20):
#    raise ValueError("Input inválido: o número de dias trabalhados deve estar entre 1 e 20")
diasTrabalhados = 20
def randomizarHorarios(horarios, n=diasTrabalhados):
    horariosRandomizados = random.sample(horarios, n)
    return horariosRandomizados

horarios = [
    ('07:51', '12:02'),
    ('07:53', '12:02'),
    ('07:58', '12:01'),
    ('07:47', '12:11'),
    ('07:51', '12:04'),
    ('07:49', '12:08'),
    ('07:58', '12:01'),
    ('07:58', '12:01'),
    ('07:58', '12:01'),
    ('07:49', '12:07'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('07:49', '12:08'),
    ('08:00', '12:05'),
    ('07:58', '12:01'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('07:45', '12:03'),
    ('07:58', '12:01'),
    ('07:58', '12:01'),
    ('07:49', '12:07'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('07:49', '12:08'),
    ('08:00', '12:05'),
    ('07:58', '12:01'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('08:00', '12:00'),
    ('07:45', '12:03'),
]
#Mistura esses horários
horariosSelecionados = randomizarHorarios(horarios)


#Loop principal
def Calculo(horariosSelecionados):
    i = 0;
    totalHorasTimeDelta = timedelta(days=0, hours=0, minutes=0, seconds=0)
    for horario in horariosSelecionados:
     i+=1
     print(f"{i}: Entrada: {horario[0]} - Saída: {horario[1]}\n")
     formato = "%H:%M"
     entrada = datetime.strptime(horario[0], formato)
     saida = datetime.strptime(horario[1], formato)
     totalHorasDia = saida - entrada
     totalHorasTimeDelta+=totalHorasDia
     print(f"Total de Horas trabalhadas no dia: {totalHorasDia}" )
    formatoTotalHoras = totalHorasTimeDelta.total_seconds() / 3600
    horas = int(formatoTotalHoras)
    minutos = int((formatoTotalHoras - horas) * 60)
    totalHoras = f"{horas:02d}:{minutos:02d}"
    print(f"\nTotal de horas trabalhadas: {totalHoras}")
    

#Chama a função de calculo
Calculo(horariosSelecionados)
exit()




