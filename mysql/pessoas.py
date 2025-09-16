import mysql.connector

# Função para criar a tabela
def criar_tabela():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="galvani3ano")
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

# Função para adicionar um novo usuário
def adicionar_usuario(nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="galvani3ano")
    cursor = conexao.cursor()
    sql = "INSERT INTO pessoas (nome, email, fone) VALUES (%s, %s, %s)"
    val = (nome, email, fone)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()




#atualizar as pessoas
def atualizar_pessoas(id, nome, email, fone):
    conexao = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="",
                                      database="galvani3ano")
    cursor = conexao.cursor()
    sql = " UPDATE pessoas SET nome = %s, email = %s, fone = %s WHERE id = %s"
    val = (nome, email, fone, id)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()


#Listar os pessoas
def listar_pessoas():
    conexao = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="",
                                      database="galvani3ano")
    cursor = conexao.cursor()
    sql = "SELECT * FROM pessoas "
    cursor.execute(sql)
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)
    conexao.close()


#Deletar o pessoa
def deletar_pessoa(id):
    conexao = mysql.connector.connect(host="localhost",
                                      user="root",
                                      password="",
                                      database="galvani3ano")
    cursor = conexao.cursor()
    sql = "DELETE FROM pessoas WHERE id =%s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()



# Função do menu de escolhas
def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    # acertei o código para o MySQL

    if escolha == '1':
        print("\nAdicionar usuário")
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        fone = input("Digite o fone do usuário: ")
        adicionar_usuario(nome, email, fone)
        print("Usuário adicionado com sucesso!")

        # daqui pra frente está com o exemplo anterior do SQLITE

    elif escolha == '2':
        print("\nListar usuários")
        listar_pessoas()
        print("Usuários listados com sucesso!")

    elif escolha == '3':
        print("\nAtualizar usuário")
        id = int(input("Digite o id do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        email = input("Digite o novo email do usuário: ")
        fone = input("Digite o novo fone do usuário: ")
        atualizar_pessoas(id, nome, email, fone)
        print("Usuário atualizado com sucesso!")

    elif escolha == '4':
        print("\nDeletar usuário")
        id = int(input("Digite o id do usuário a ser deletado: "))
        deletar_pessoa(id)
        print("Usuário deletado com sucesso!")

    elif escolha == '5':
        print("\nSair")
        break

        #ver o exemplo do programa de CRUD SQLITE
