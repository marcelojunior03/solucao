from datetime import datetime

hoje = datetime.today()

print("Olá, seja muito bem-vindo(a)! Lembre-se que para obter melhores resultados, é importante ter acompanhamento profissional!\n")
nome = input("Por favor, me diga o seu nome completo:\n")
nascimento = input("Agora, insira sua data de nascimento (no modelo dd/mm/aaaa):\n")
nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
idade = hoje.year - nascimento.year
if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
    idade -= 1

