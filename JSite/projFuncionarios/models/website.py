from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String)

engine = create_engine('sqlite:///web.db', echo = True)
metadata = MetaData(bind=engine)
tabelaDeUsuarios = Table('usuarios', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('nome', String(40), index=True),
                   Column('sobrenome', String(40), index=True),
                   Column('cpf', String(40), index=True),
                   Column('tempoDeServico', Integer, nullable=False),
                   Column('remuneracao', Integer, nullable=False))

metadata.create_all()
