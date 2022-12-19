from website import tabelaDeUsuarios
from sqlalchemy import select

selecionar = select([tabelaDeUsuarios])

for dadosDoUsuario in selecionar.execute():
    print(dadosDoUsuario)
