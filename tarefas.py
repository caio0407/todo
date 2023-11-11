import os 


def criar_tarefa(cursor,conexao):
    os.system('cls')
    print("-- CRIAÇÃO DE TAREFA --\n")
    nome=input('Nome: ')
    data=input('Data (dd/mm/aaaa): ')
    categoria_id=int(input('Categoria (ID): '))
    sql_criar_tarefa="INSERT INTO todo (nome,data,categoria_id) VALUES (?,?,?);"
    cursor.execute(sql_criar_tarefa, [nome,data,categoria_id])
    conexao.commit()
    print('Tarefa inserida')
    input()


def deletar_tarefa(cursor,conexao):
    os.system('cls')
    print('--EXCLUSÃO DE TAREFA--\n')
    id_tarefa =int(input("ID da Tarefa: "))
    sql_deletar_tarefa = "DELETE FROM todo WHERE id= ?;"
    cursor.execute(sql_deletar_tarefa,[id_tarefa])
    conexao.commit()
    print('Tarefa excluída')
    input()


def atualizar_tarefa(cursor,conexao):   
    os.system('cls')
    print("-- ATUALIZAÇÃO DE TAREFA--\n")
    id_tarefa =int(input("ID da Tarefa: "))
    novo_nome_tarefa = input("Novo Nome da Tarefa: ")
    nova_data_tarefa =input('Nova Data (dd/mm/aaaa): ')
    nova_categoria_id =int(input('Nova Categoria (ID): '))
    sql_atualizar_tarefa = "UPDATE todo SET nome= ?,data= ?,categoria_id=? WHERE id= ?;"
    cursor.execute(sql_atualizar_tarefa, (novo_nome_tarefa,nova_data_tarefa,nova_categoria_id,id_tarefa))
    conexao.commit()
    print('Tarefa Atualizada')
    input()
    
 
def listar_tarefa(cursor):
    os.system('cls')
    print('-- LISTAGEM DAS TAREFAS--\n')
    cursor.execute("""SELECT t.id, t.nome, t.data, c.nome, CASE WHEN status=1 THEN 'Sim' ELSE 'Não' END  
                  FROM todo t JOIN categoria c ON c.id=t.categoria_id;""")
    tarefas= cursor.fetchall()
    for tarefa in tarefas:
        print(f"ID: {tarefa[0]}, Nome: {tarefa[1]}, Data: {tarefa[2]}, Status: {tarefa[4]}, Categoria: {tarefa[3]}")
    input()
    
def concluir_tarefa(cursor,conexao):
    os.system('cls')
    print("-- CONCLUSAO DE TAREFA--\n")
    id_tarefa =int(input("ID da Tarefa: ")) 
    cursor.execute("UPDATE todo SET status=1 WHERE id=?",[id_tarefa])
    conexao.commit()
    print('Tarefa Concluida')
    input()
    
def listar_tarefa_por_dia(cursor):
    os.system('cls')
    print('-- LISTAGEM DAS TAREFAS POR DIA --\n')
    data=input('Data (dd/mm/aaa): ')
    cursor.execute("""SELECT t.id, t.nome, t.data, c.nome ,CASE WHEN status=1 THEN 'Sim' ELSE 'Não' END  
                  FROM todo t JOIN categoria c ON c.id=t.categoria_id WHERE data=?;""",[data])
    tarefas= cursor.fetchall()
    for tarefa in tarefas:
        print(f"ID: {tarefa[0]}, Nome: {tarefa[1]}, Data: {tarefa[2]}, Status: {tarefa[4]}, Categoria: {tarefa[3]}")
    input()
    
def menu(conexao,cursor):
    while True: 
        os.system('cls')
        print('''--TAREFAS--\n
            (1) CRIAR
            (2) LISTAR
            (3) LISTAR POR DIA
            (4) DELETAR
            (5) ATUALIZAR
            (6) CONCLUIR TAREFA
            (0) MENU PRINCIPAL
            ''')
        opcao= input('Opção: ')
        
        if opcao == '1':
            criar_tarefa(cursor,conexao)
        elif opcao == '2':
            listar_tarefa(cursor)
        elif opcao == '3':
            listar_tarefa_por_dia(cursor) 
        elif opcao == '4':
            deletar_tarefa(cursor, conexao)  
        elif opcao == '5':
            atualizar_tarefa(cursor, conexao)
        elif opcao == '6':
            concluir_tarefa(cursor, conexao)
        elif opcao == '0':
            break
        else: 
            print('Opção inválida!')
            input()              

