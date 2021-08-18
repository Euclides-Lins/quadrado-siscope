import sqlite3

connection = sqlite3.connect("../list-siscope.db")

def createTable():
    cursor = connection.cursor();
    connection.execute("""
    create table if not exists produto (
        codigo text,
        nome text,
        descricao text,
        preco float,
        desconto float,
        quantidade integer
    )
    """)

def postProduto(produto):
    connection.execute("insert into produto (codigo, nome, descricao, preco, desconto, quantidade) values (?, ?, ?, ?, ?, ?)", \
     (produto.codigo, produto.nome, produto.descricao, produto.preco, produto.desconto, produto.quantidade ))
    connection.commit()

def deleteProduto(codigo):
    connection.execute("delete from produto where codigo = ?", (codigo,))
    connection.commit()

def updateProduto(produto):
    connection.execute("update produto set nome = ?, descricao = ?, preco = ?, desconto = ?, quantidade = ?", \
    (produto.nome, produto.descricao, produto.preco, produto.desconto, preco.quantidade))
    connection.commit()

def getProduto():
    return connection.execute("select * from produto")    