import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk

# Configuração da conexão com o MySQL
def conectar():
    return mysql.connector.connect(
        host="localhost",      
        user="root",           
        password="",   
        database="repertorio"  
    )

def criar_banco():
    conexao = conectar()
    ponteiro = conexao.cursor()
    ponteiro.execute('''
        CREATE TABLE IF NOT EXISTS faixa (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            cantor VARCHAR(255),
            tags VARCHAR(255),
            disco VARCHAR(255),
            estilo VARCHAR(100),
            ano_lancamento INT,
            tempo_segundos INT,
            autor VARCHAR(255),
            produtora VARCHAR(255),
            local_arquivo VARCHAR(500)
        )
    ''')
    conexao.commit()
    conexao.close()

def inserir_faixa(nome, cantor, tags, disco, estilo, ano_lancamento, tempo_segundos, autor, produtora, local_arquivo):
    conexao = conectar()
    ponteiro = conexao.cursor()
    ponteiro.execute('''
        INSERT INTO faixa (nome, cantor, tags, disco, estilo, ano_lancamento, tempo_segundos, autor, produtora, local_arquivo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (nome, cantor, tags, disco, estilo, int(ano_lancamento), int(tempo_segundos), autor, produtora, local_arquivo))
    conexao.commit()
    conexao.close()

def listar_faixas():
    conexao = conectar()
    ponteiro = conexao.cursor()
    ponteiro.execute('SELECT * FROM faixa')
    resultado = ponteiro.fetchall()
    conexao.close()
    return resultado

def remover_faixa(codigo):
    conexao = conectar()
    ponteiro = conexao.cursor()
    ponteiro.execute('DELETE FROM faixa WHERE codigo = %s', (codigo,))
    conexao.commit()
    conexao.close()

def atualizar_faixa(codigo, nome, cantor, tags, disco, estilo, ano_lancamento, tempo_segundos, autor, produtora, local_arquivo):
    conexao = conectar()
    ponteiro = conexao.cursor()
    ponteiro.execute('''
        UPDATE faixa
        SET nome = %s, cantor = %s, tags = %s, disco = %s, estilo = %s, ano_lancamento = %s, tempo_segundos = %s, autor = %s, produtora = %s, local_arquivo = %s
        WHERE codigo = %s
    ''', (nome, cantor, tags, disco, estilo, int(ano_lancamento), int(tempo_segundos), autor, produtora, local_arquivo, codigo))
    conexao.commit()
    conexao.close()


# --- GUI ---
def janela_inserir():
    def salvar():
        try:
            inserir_faixa(
                nome.get(),
                cantor.get(),
                tags.get(),
                disco.get(),
                estilo.get(),
                int(ano_lancamento.get()),
                int(tempo.get()),
                autor.get(),
                produtora.get(),
                local.get()
            )
            messagebox.showinfo("Sucesso", "Faixa adicionada!")
            popup.destroy()
            atualizar_tabela()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    popup = tk.Toplevel(janela_principal)
    popup.title("Adicionar Faixa")

    campos = ["Nome", "Cantor", "Tags", "Disco", "Estilo", "Ano", "Duração (seg)", "Autor", "Produtora", "Local do Arquivo"]

    nome = tk.Entry(popup)
    cantor = tk.Entry(popup)
    tags = tk.Entry(popup)
    disco = tk.Entry(popup)
    estilo = tk.Entry(popup)
    ano_lancamento = tk.Entry(popup)
    tempo = tk.Entry(popup)
    autor = tk.Entry(popup)
    produtora = tk.Entry(popup)
    local = tk.Entry(popup)

    entradas = [nome, cantor, tags, disco, estilo, ano_lancamento, tempo, autor, produtora, local]

    for i, campo in enumerate(campos):
        tk.Label(popup, text=campo).grid(row=i, column=0, sticky="w")
        entradas[i].grid(row=i, column=1)

    tk.Button(popup, text="Salvar", command=salvar).grid(row=len(campos), columnspan=2)

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    for linha in listar_faixas():
        tabela.insert("", "end", values=linha)

def excluir_faixa():
    item = tabela.selection()
    if item:
        codigo = tabela.item(item[0])['values'][0]
        remover_faixa(codigo)
        atualizar_tabela()
        messagebox.showinfo("Sucesso", "Faixa removida.")
    else:
        messagebox.showwarning("Atenção", "Selecione uma faixa.")

def editar_faixa():
    item = tabela.selection()
    if not item:
        messagebox.showwarning("Atenção", "Selecione uma faixa.")
        return

    dados = tabela.item(item[0])['values']
    codigo = dados[0]

    def salvar():
        try:
            atualizar_faixa(
                codigo,
                nome.get(),
                cantor.get(),
                tags.get(),
                disco.get(),
                estilo.get(),
                int(ano_lancamento.get()),
                int(tempo.get()),
                autor.get(),
                produtora.get(),
                local.get()
            )
            messagebox.showinfo("Sucesso", "Faixa atualizada!")
            popup.destroy()
            atualizar_tabela()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    popup = tk.Toplevel(janela_principal)
    popup.title("Editar Faixa")

    campos = ["Nome", "Cantor", "Tags", "Disco", "Estilo", "Ano", "Duração (seg)", "Autor", "Produtora", "Local do Arquivo"]
    valores = dados[1:]

    nome = tk.Entry(popup)
    cantor = tk.Entry(popup)
    tags = tk.Entry(popup)
    disco = tk.Entry(popup)
    estilo = tk.Entry(popup)
    ano_lancamento = tk.Entry(popup)
    tempo = tk.Entry(popup)
    autor = tk.Entry(popup)
    produtora = tk.Entry(popup)
    local = tk.Entry(popup)

    entradas = [nome, cantor, tags, disco, estilo, ano_lancamento, tempo, autor, produtora, local]

    for i, campo in enumerate(campos):
        tk.Label(popup, text=campo).grid(row=i, column=0, sticky="w")
        entradas[i].insert(0, valores[i])
        entradas[i].grid(row=i, column=1)

    tk.Button(popup, text="Salvar Alterações", command=salvar).grid(row=len(campos), columnspan=2)


# --- Inicialização ---
criar_banco()

janela_principal = tk.Tk()
janela_principal.title("Gerenciador de Faixas (MySQL)")

tabela = ttk.Treeview(janela_principal, columns=('ID', 'Nome', 'Cantor', 'Tags', 'Disco', 'Estilo', 'Ano', 'Duração', 'Autor', 'Produtora', 'Local'), show='headings')

for col in tabela["columns"]:
    tabela.heading(col, text=col)
    tabela.column(col, width=100, anchor="w")

tabela.pack(fill=tk.BOTH, expand=True)

frame_botoes = tk.Frame(janela_principal)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Adicionar", command=janela_inserir).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Editar", command=editar_faixa).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir_faixa).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="Sair", command=janela_principal.destroy).grid(row=0, column=3, padx=5)

atualizar_tabela()
janela_principal.mainloop()
