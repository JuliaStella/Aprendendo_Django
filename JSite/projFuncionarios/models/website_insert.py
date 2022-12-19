from website import tabelaDeUsuarios, engine

conn = engine.connect()
inserir = tabelaDeUsuarios.insert()

conn.execute(tabelaDeUsuarios.insert(), [
    #{'nome': 'Silva', 'sobrenome': 'Silva', 'cpf': '123.456.789-11', 'tempoDeServico': 6, 'remuneracao': 2000},
    {'nome': 'Silva', 'sobrenome': 'Silva', 'cpf': '123.456.789-11', 'tempoDeServico': 3, 'remuneracao': 2000},
    {'nome': 'Jaca', 'sobrenome': 'Silva', 'cpf': '123.496.789-11', 'tempoDeServico': 9, 'remuneracao': 4000},
    {'nome': 'b', 'sobrenome': 'jc', 'cpf': '193.456.789-40', 'tempoDeServico': 5, 'remuneracao': 5000},
    {'nome': 'c', 'sobrenome': 'pd', 'cpf': '233.456.789-90', 'tempoDeServico': 4, 'remuneracao': 6000},
    {'nome': 'd', 'sobrenome': 'pc', 'cpf': '893.456.789-74', 'tempoDeServico': 7, 'remuneracao': 7000},
    {'nome': 'e', 'sobrenome': 'pg', 'cpf': '523.456.489-01', 'tempoDeServico': 8, 'remuneracao': 8000},
    {'nome': 'f', 'sobrenome': 'gp', 'cpf': '123.476.799-16', 'tempoDeServico': 8, 'remuneracao': 9000},
    {'nome': 'g', 'sobrenome': 'ab', 'cpf': '143.458.786-13', 'tempoDeServico': 9, 'remuneracao': 23000},
    {'nome': 'h', 'sobrenome': 'ad', 'cpf': '123.456.735-11', 'tempoDeServico': 12, 'remuneracao': 25000},
])