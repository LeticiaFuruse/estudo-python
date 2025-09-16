# Crie um programa em Python onde o usuário irá escolher 1 entre 4 destinos de
# viagens de avião através de uma ComboBox e depois irá escolher o tipo de assento
# no voo, sendo Primeira Classe (mais cara), Executiva (preço intermediário) e
# Econômica (mais barata). Esta escola do tipo do assento deve ser escolhida por um
# botão de rádio. Imprima o VALOR da PASSAGEM.

import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário com valores base de cada destino
destinos = {
    "São Paulo": 500,
    "Rio de Janeiro": 650,
    "Salvador": 900,
    "Fortaleza": 1200
}

# Função para calcular o preço da passagem
def calcular_passagem():
    destino = combo_destino.get()
    assento = var_assento.get()
    
    if destino == "Selecione":
        messagebox.showwarning("Aviso", "Escolha um destino!")
        return
    if assento == "":
        messagebox.showwarning("Aviso", "Escolha o tipo de assento!")
        return
    
    preco_base = destinos[destino]
    
    # Multiplicadores do preço de acordo com o assento
    if assento == "Primeira Classe":
        preco = preco_base * 2.0
    elif assento == "Executiva":
        preco = preco_base * 1.5
    else:  # Econômica
        preco = preco_base * 1.0
    
    label_resultado.config(text=f"Valor da passagem: R${preco:.2f}")

# Janela principal
janela = tk.Tk()
janela.title("Compra de Passagem Aérea")
janela.geometry("350x300")

# Destino
tk.Label(janela, text="Escolha o destino:").pack(pady=5)
combo_destino = ttk.Combobox(janela, values=list(destinos.keys()), state="readonly")
combo_destino.pack(pady=5)
combo_destino.set("Selecione")

# Tipo de assento
tk.Label(janela, text="Escolha o tipo de assento:").pack(pady=5)
var_assento = tk.StringVar(value="")

tk.Radiobutton(janela, text="Primeira Classe", variable=var_assento, value="Primeira Classe").pack(anchor="w")
tk.Radiobutton(janela, text="Executiva", variable=var_assento, value="Executiva").pack(anchor="w")
tk.Radiobutton(janela, text="Econômica", variable=var_assento, value="Econômica").pack(anchor="w")

# Botão para calcular
btn_calcular = tk.Button(janela, text="Calcular Valor", command=calcular_passagem)
btn_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="Valor da passagem: R$0,00", font=("Arial", 12, "bold"))
label_resultado.pack(pady=10)

# Loop da aplicação
janela.mainloop()
