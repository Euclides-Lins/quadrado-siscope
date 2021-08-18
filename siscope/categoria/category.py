import sqlite3

connection = sqlite3.connect('../list-siscope.db')

class Categoria:
    def __init__(self, codigo, nome, ativo):
        self.codigo = codigo
        self.nome = nome
        self.ativo = ativo

def createTable():
    cursor = connection.cursor()
    connection.execute("""
        create table if not exists categoria (
            codigo integer primary key,
            nome text,
            ativo bool
        )
    """)


def postCategoria(categoria):
    connection.execute(
        "insert into categoria (codigo, nome, ativo) values (?, ?, ?)", \
        (categoria.codigo, categoria.nome, categoria.ativo)            \
    )
    connection.commit()
    
def deleteCategoria(codigo):
    connection.execute("delete from categoria where codigo = ?", (codigo,))
    connection.commit()
    
def updateCategoria(categoria):
    connection.execute("update categoria set nome = ?, ativo = ? where codigo = ?", (categoria.nome, categoria.ativo, categoria.codigo))
    connection.commit()
    
def getCategoria():
    return connection.execute("select * from categoria")