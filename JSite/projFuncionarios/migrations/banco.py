import sqlite3
con = sqlite3.connect('g.db')
cur = con.cursor()

sql = """CREATE TABLE s(
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL,
           sobrenome TEXT NOT NULL,
           cpf TEXT NOT NULL,
           tempoDeServico INTEGER NOT NULL,
           remuneracao INTEGER  NOT NULL)"""
cur.execute(sql)
con.commit()
con.close()