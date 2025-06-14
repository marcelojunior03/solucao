import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_tempo_perdido():
    try:
        nome = entrada_nome.get()
        nascimento_str = entrada_nascimento.get()
        inicio_idade = int(entrada_inicio_idade.get())
        cigarros_dia = int(entrada_cigarros.get())

        nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - nascimento.year
        if hoje.month < nascimento.month or (hoje.month == nascimento.month and hoje.day < nascimento.day):
            idade -= 1

        tempo_fumando = idade - inicio_idade
        cigarros_fumados = (cigarros_dia*365)*tempo_fumando
        tempo_perdido = cigarros_fumados*20

        resultado.config(text=f"{nome}, até agora você perdeu cerca de {tempo_perdido:.0f} minutos de vida...\nMas calma, vamos te ajudar!")

    except ValueError:
        messagebox.showerror("Erro", "Verifique os dados inseridos. Use o formato correto e apenas números.")

janela = tk.Tk()
janela.title("Calculadora de Tempo Perdido")
janela.geometry("700x600")

boasvindas = tk.Label(janela, text="Olá, seja muito bem-vindo(a)!\nLembre-se de procurar ajuda profissional!", font=("Arial", 12))
rotulo_nome = tk.Label(janela, text="Digite seu nome completo:", font=("Arial", 12))
entrada_nome = tk.Entry(janela, width=30, font=("Arial", 12))
rotulo_data = tk.Label(janela, text="Digite sua data de nascimento (dd/mm/aaaa):", font=("Arial", 12))
entrada_nascimento = tk.Entry(janela, width=15, font=("Arial", 12))
rotulo_inicio = tk.Label(janela, text="Com quantos anos você começou a fumar?", font=("Arial", 12))
entrada_inicio_idade = tk.Entry(janela, width=5, font=("Arial", 12))
rotulo_cigarros = tk.Label(janela, text="Em média, quantos cigarros por dia?", font=("Arial", 12))
entrada_cigarros = tk.Entry(janela, width=5, font=("Arial", 12))
bt = tk.Button(janela, text="Calcular", command=calcular_tempo_perdido, font=("Arial", 10))
resultado = tk.Label(janela, text="", font=("Arial", 12))

boasvindas.pack(pady=10)
rotulo_nome.pack(pady=10)
entrada_nome.pack(pady=5)
rotulo_data.pack(pady=10)
entrada_nascimento.pack(pady=5)
rotulo_inicio.pack(pady=10)
entrada_inicio_idade.pack(pady=5)
rotulo_cigarros.pack(pady=10)
entrada_cigarros.pack(pady=5)
bt.pack(pady=10)
resultado.pack(pady=10)

janela.mainloop()
