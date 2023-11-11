import sqlite3
import os
import categorias
import tarefas

def criar_tabelas(cursor):
    os.system('cls')
    print("-- CRIAÇÃO DAS TABELAS --\n")
    sql_categoria = '''
    CREATE TABLE categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL
    );
    '''

    sql_todo = '''
    CREATE TABLE todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,    
        data VARCHAR(10) NOT NULL,
        status INTEGER NOT NULL DEFAULT (0),
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
    );
    '''
    try:
        cursor.execute(sql_categoria)
        cursor.execute(sql_todo)
        print('tabelas criadas')
        input()
    except sqlite3.OperationalError:
        print("tabelas ja´existentes")
        input()


conexao=sqlite3.connect('bancodedados.sqlite3')
cursor=conexao.cursor()

while True:
    os.system("cls")
    print('--TODO--\n\n(1) Criar Tabelas\n(2) Categorias\n(3) Tarefas\n(0) Sair\n')
    opcao=input("OPÇÃO: ")
    if opcao== "1":
         criar_tabelas(cursor)
    elif opcao== "2":
        categorias.menu(conexao,cursor)
    elif opcao== "3":
        tarefas.menu(conexao,cursor)
    elif opcao== "0":
        print('ATÉ MAIS ')
        break
    else:
        print('OPÇÕES INVALÍDAS')
        input()
        
conexao.commit()
conexao.close()