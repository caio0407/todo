import os

        
def criar_categoria(cursor,conexao):
    os.system('cls')
    print("-- CRIAÇÃO DE CATEGORIA --\n")
    nome_categoria = input("Nome da Categoria: ")
    sql_criar_categoria= "INSERT INTO categoria (nome) VALUES (?);"
    cursor.execute(sql_criar_categoria, [nome_categoria])
    conexao.commit()
    print('Categoria inserida')
    input()
    
def deletar_categoria(cursor,conexao):
    os.system('cls')
    print('--EXCLUSÃO DE CATEGORIA--\n')
    id_categoria =int(input("ID da Categoria: "))
    sql_deletar_categoria = "DELETE FROM categoria WHERE id= ?;"
    cursor.execute(sql_deletar_categoria, [id_categoria])
    conexao.commit()
    print('Categoria excluída')
    input()
    
def atualizar_categoria(cursor,conexao):
    os.system('cls')
    print("-- ATUALIZAÇÃO DE CATEGORIA--\n")
    id_categoria =int(input("ID da Categoria: "))
    novo_nome_categoria = input("Novo Nome da Categoria: ")
    sql_atualizar_categoria = "UPDATE categoria SET nome= ? WHERE id= ?;"
    cursor.execute(sql_atualizar_categoria, (novo_nome_categoria,id_categoria))
    conexao.commit()
    print('Categoria Atualizada')
    input()
    
def listar_categoria(cursor):
    os.system('cls')
    print('-- LISTAGEM DAS CATEGORIAS--\n')
    cursor.execute("SELECT * FROM categoria;")
    categorias= cursor.fetchall()
    #print(categorias)
    for categoria in categorias:
        print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
    input()
                
def menu(conexao,cursor):
    while True: 
        os.system('cls')
        print('''--CATEGORIAS--\n
            (1) CRIAR
            (2) LISTAR
            (3) DELETAR
            (4) ATUALIZAR
            (0) MENU PRINCIPAL
            ''')
        opcao= input('Opção: ')
        
        if opcao == '1':
            criar_categoria(cursor,conexao)
        elif opcao == '2':
            listar_categoria(cursor)  
        elif opcao == '3':
            deletar_categoria(cursor, conexao)  
        elif opcao == '4':
            atualizar_categoria(cursor, conexao)
        elif opcao == '0':
            break
        else: 
            print('Opção inválida!')
            input()                    

