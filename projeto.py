from datetime import datetime

hoje = datetime.today()

nome = input("Olá, seja muito bem-vindo(a)! Por favor, me diga o seu nome completo:\n")
nascimento = input("Agora, insira sua data de nascimento (no modelo dd/mm/aaaa):\n")
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
idade = hoje.year - nascimento.year
if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
    idade -= 1

