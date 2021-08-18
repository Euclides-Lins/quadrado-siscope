import sqlite3

connection = sqlite3.connect("../list-siscope.db")

class Setor:
    def __init__(self, codigo, nome, sigla, ativo):
        self.codigo = codigo
        self.nome = nome
        self.sigla = sigla
        self.ativo = ativo


def createTable():
    cursor = connection.cursor();
    connection.execute("""
    create table if not exists setor (
        codigo text,
        nome text,
        sigla float,
        ativo bool,
    )
    """)

def postSetor(setor):
    connection.execute(
        "insert into setor (codigo, nome, sigla, ativo) values (?, ?, ?, ?)", \
        (setor.codigo, setor.nome, setor.sigla,setor.ativo)            \
    )
    connection.commit()
    
def deleteSetor(codigo):
    connection.execute("delete from setor where codigo = ?", (codigo,))
    connection.commit()
    
def updateSetor(setor):
    connection.execute("update setor set nome = ?, sigla = ?,ativo = ? where codigo = ?", (categoria.nome, categoria.ativo, categoria.codigo))
    connection.commit()
    
def getSetor():
    return connection.execute("select * from setor")