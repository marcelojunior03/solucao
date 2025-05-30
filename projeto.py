from datetime import datetime

hoje = datetime.today()

print("Olá, seja muito bem-vindo(a)! Lembre-se que para obter melhores resultados, é importante ter acompanhamento profissional!\n")

nome = input("Por favor, me diga o seu nome completo:\n")

nascimento = input("Agora, insira sua data de nascimento (no modelo dd/mm/aaaa):\n")
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
idade = hoje.year - nascimento.year
if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
    idade -= 1

inicio_idade = float(input("Com quantos anos você começou a fumar?"))
tempo_fumando = idade - inicio_idade

cigarros_dia = int(input("Em média, quantos cigarros você fuma por dia?"))

cigarros_fumados = (cigarros_dia*365)*tempo_fumando

tempo_perdido = cigarros_fumados*20

print(f"Até agora, você perdeu cerca de {tempo_perdido} minutos de vida... Mas calma, vamos te ajudar!")