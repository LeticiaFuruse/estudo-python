import sqlite3

#CRIANDO TABELA
def criar_tabela():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute (''' CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL)''')
    conexao.commit()
    conexao.close()


#Adicionar um novo usuario
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute(''' INSERT INTO usuarios (nome, idade) VALUES (?, ?) ''', (nome, idade))

    conexao.commit()
    conexao.close()

#Atualizar o usuario
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute(''' UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?''', (nome, idade, id))
    
    conexao.commit()
    conexao.close()

#Listar os usuarios
def listar_usuarios():
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(usuario)

    conexao.close()

#Deletar o usuario
def deletar_usuario(id):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute(''' DELETE FROM usuarios WHERE id = ?''', (id,))
    
    conexao.commit()
    conexao.close()


#Pesquisa usuario que são menores que uma determinada idade digitada pelo usuario
def pesquisa_idadeMenor(idade):
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    cursor.execute(
        '''SELECT * FROM usuarios WHERE idade <= ? ''', (idade,)
    )

    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

    conexao.close()


# Função do menu de escolhas 
def menu():
    print("\n1 - Adicionar um novo usuario")
    print("\n2 - Listar todos os usuarios")
    print("\n3 - Atualizar um usuario")
    print("\n4 - Deletar um usuario")
    print("\n5 - Pesquisar um usuario pela idade menor ou igual a idade digitada")
    print("\n6 - Sair")

#Função para criar tabela (se ainda não existir)
criar_tabela()


#Função para escolha de menus
while True:
    menu()
    escolha = input ("Escolha uma opção:")

    if escolha == '1':
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        adicionar_usuario(nome, idade)
        print ("Usuario adicionado com sucesso")

    elif escolha == '2':
        print("\nTodos os usuarios:")
        listar_usuarios()
    
    elif escolha == '3':
        id = int(input("Digite o ID do usuario a ser atualizado: "))
        nome = input("Digite o novo nome do usuario: ")
        idade = int(input("Digite a nova idade do usuario: "))
        atualizar_usuario(id, nome, idade)
        print("Usuario atualizado com sucesso")

    elif escolha == '4':
        id = int(input("Digite o id do usuario deletado: "))
        deletar_usuario(id)
        print("Usuario deletado com sucesso")


    elif escolha == '5':
        idade = int(input("Digite a idade:"))
        pesquisa_idadeMenor(idade)
        print("Usuarios menores/iguais que a idade digitada")


    elif escolha == '6':
        print("Saindo...")
        break

    else:
        print("Opção inválida, escolha uma opção valida")
        

