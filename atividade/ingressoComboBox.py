import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Janela principal
janela = tk.Tk()
janela.title("Comprar ingressos")
janela.geometry("300x300")

# Label da quantidade
tk.Label(janela, text="Escolha a quantidade de ingressos:").pack(pady=5)
# Lista de opções
opcoes_qtde = [str(i) for i in range(1, 11)]

# Combobox da quantidade
combo_qtde = ttk.Combobox(janela, values=opcoes_qtde, state="readonly")
combo_qtde.pack(pady=5)
combo_qtde.set("Selecione")

# Label do tipo de ingresso
tk.Label(janela, text="Escolha o tipo de ingresso:").pack(pady=5)
# Lista de opções
opcoes_tipo = ["Inteira", "Meia", "Idoso", "Criança"]

# Combobox do tipo
combo_tipo = ttk.Combobox(janela, values=opcoes_tipo, state="readonly")
combo_tipo.pack(pady=5)
combo_tipo.set("Selecione")

# Label de resultado
label_resultado = tk.Label(janela, text="Total a pagar: R$0,00")
label_resultado.pack(pady=10)

# Função para calcular ingressos 
def calcular_ingressos():
    try:
        ingresso = 20
        qtde = int(combo_qtde.get())
        tipo = combo_tipo.get()
        
        if tipo == 'Inteira':
            valor_unit = ingresso
        elif tipo == "Meia":
            valor_unit = ingresso * 0.5
        elif tipo == "Idoso":
            valor_unit = ingresso * 0.4
        elif tipo == "Criança":
            valor_unit = 0
        else:
            messagebox.showwarning("Aviso", "Escolha um tipo de ingresso válido!")
            return
        
        resultado = valor_unit * qtde
        label_resultado.config(text=f"Total a Pagar: R${resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, selecione uma quantidade válida.")

# Função ao clicar no botão
def mostrar_escolha():
    quantidade = combo_qtde.get()
    tipo = combo_tipo.get()
    if quantidade == "Selecione" or tipo == "Selecione":
        messagebox.showwarning("Aviso", "Você precisa escolher quantidade e tipo!")
    else:
        calcular_ingressos()
        messagebox.showinfo("Seu ingresso", f"Você escolheu {quantidade} ingresso(s) - {tipo} - Total: {label_resultado.cget('text')}")

# Botão para confirmar escolha
botao = tk.Button(janela, text="Confirmar", command=mostrar_escolha)
botao.pack(pady=10)

# Loop da aplicação
janela.mainloop()
