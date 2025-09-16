import sqlite3


#CRIANDO TABELA musicas
def criar_tabela():
    conexao = sqlite3.connect('musicas.db')
    cursor = conexao.cursor()
    cursor.execute (''' CREATE TABLE IF NOT EXISTS musicas(
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    artistas TEXT,
                    palavras_chaves TEXT,
                    album TEXT,
                    genero TEXT,
                    ano INTEGER,
                    duracao_segundos INTEGER,
                    compositor TEXT,
                    gravadora TEXT,
                    caminho_arquivo TEXT
                    )''')
    conexao.commit()
    conexao.close()


# adicionar musicas
def adicionar_musicas(titulo, artistas, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('musicas.db')
    cursor = conexao.cursor()
    cursor.execute(''' INSERT INTO musicas (titulo, artistas, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ''', (titulo, artistas, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo))

    conexao.commit()
    conexao.close()


#listar as musicas
def atualizar_musicas(id, titulo, artistas, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo):
    conexao = sqlite3.connect('musicas.db')
    cursor = conexao.cursor()
    cursor.execute(''' UPDATE musicas SET titulo = ?, artistas = ?, palavras_chaves = ?, album = ?, genero = ?, ano = ?, duracao_segundos = ?, compositor = ?, gravadora = ?, caminho_arquivo = ? WHERE id = ?''', (titulo, artistas, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo, id))
    
    conexao.commit()
    conexao.close()


#Listar os musicas
def listar_musicas():
    conexao = sqlite3.connect('musicas.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM musicas''')
    musicas = cursor.fetchall()

    for musica in musicas:
        print(musica)

    conexao.close()


#Deletar o musica
def deletar_musica(id):
    conexao = sqlite3.connect('musicas.db')
    cursor = conexao.cursor()
    cursor.execute(''' DELETE FROM musicas WHERE id = ?''', (id,))
    
    conexao.commit()
    conexao.close()


# Função do menu de escolhas 
def menu():
    print("\n1 - Adicionar uma nova musica")
    print("\n2 - Listar todas as musicas")
    print("\n3 - Atualizar uma musica")
    print("\n4 - Deletar uma musica")
    print("\n5 - Sair")


#Função para criar tabela (se ainda não existir)
criar_tabela()




#Função para escolha de menus
while True:
    menu()
    escolha = input ("Escolha uma opção:")

    if escolha == '1':
        titulo = input("Digite o titulo: ")
        artista = input("Digite a artista: ")
        palavras_chaves = input("Digite as palavras chaves: ")
        album = input("Digite o album: ")
        genero = input("Digite o genero: ")
        ano = int(input("Digite o ano: "))
        duracao_segundos = int(input("Digite a duracao em segundos: "))
        compositor = input("Digite o compositor: ")
        gravadora = input("Digite a gravadora: ")
        caminho_arquivo = input("Digite o caminho do arquivo: ")

        adicionar_musicas(titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo)
        print ("Musica adicionada com sucesso")

    elif escolha == '2':
        print("\nTodas as musicas:")
        listar_musicas()
    
    elif escolha == '3':
        id = int(input("Digite o ID do usuario a ser atualizado: "))
        titulo = input("Digite o novo titulo da musica: ")
        artista = input("Digite a nova artista da musicapython: ")
        palavras_chaves = input("Digite as palavras chaves: ")
        album = input("Digite o album:")
        genero = input("Digite o genero: ")
        ano = int(input("Digite o ano:"))
        duracao_segundos = int(input("Digite a duração em segundos: "))
        compositor = input("Digite o compositor: ")
        gravadora = input("Digite a gravador:")
        caminho_arquivo = input("Digite o caminho do arquivo:")
    
        atualizar_musicas(id, titulo, artista, palavras_chaves, album, genero, ano, duracao_segundos, compositor, gravadora, caminho_arquivo)
        print("Musica atualizada com sucesso")

    elif escolha == '4':
        id = int(input("Digite o id da musica para deletar: "))
        deletar_musica(id)
        print("Musica deletado com sucesso")


    elif escolha == '5':
        print("Saindo...")
        break

    else:
        print("Opção inválida, escolha uma opção valida")
        

