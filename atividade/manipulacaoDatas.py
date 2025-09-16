from datetime import datetime
import tkinter as tk

# Transforme este programa textual em um programa gráfico utilizando Tkinter, mostrando a
# diferença em dias entre 2 datas.



# Função para calcular a diferença entre as datas
def calcular_diferenca():
    data1 = entrada_data1.get()
    data2 = entrada_data2.get()
    formato = "%d/%m/%Y"
    try:
        d1 = datetime.strptime(data1, formato)
        d2 = datetime.strptime(data2, formato)
        diferenca = abs((d2 - d1).days)
        resultado_label.config(text=f"Diferença em dias: {diferenca}")
    except ValueError:
        resultado_label.config(text="Formato inválido! Use dd/mm/yyyy")

# abrir janela
janela = tk.Tk()
janela.title("Manipulacao de Dados")


# Widgets
tk.Label(janela, text="Data 1 (dd/mm/yyyy):").grid(row=0, column=0, padx=5, pady=5)
entrada_data1 = tk.Entry(janela, width=20)
entrada_data1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(janela, text="Data 2 (dd/mm/yyyy):").grid(row=1, column=0, padx=5, pady=5)
entrada_data2 = tk.Entry(janela, width=20)
entrada_data2.grid(row=1, column=1, padx=5, pady=5)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular_diferenca)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

resultado_label = tk.Label(janela, text="Digite duas datas para calcular.")
resultado_label.grid(row=3, column=0, columnspan=2, pady=5)

# Inicia o loop da janela
janela.mainloop()