import sqlite3

con = sqlite3.connect('baseDeDados.db') #criando base
cur = con.cursor() #conectado cursor

#sintaxe do sql

sql = """
CREATE TABLE funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         nome TEXT NOT NULL,
         sobrenome TEXT NOT NULL,
         cpf TEXT NOT NULL,
         remuneracao INTERGER UNIQUE NOT NULL) 
"""
cur.execute(sql)
con.commit() # executar os comandos na nossa base
con.close()