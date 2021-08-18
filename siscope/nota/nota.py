import sqlite3

connection = sqlite3.connect("../list-siscope.db")

def createTable():
    cursor = connection.cursor();
    connection.execute("""
    create table if not exists nota (
        numero text,
        data text,
        subtotal float,
        desconto float,
        total float,
        qntdProdutos integer,
        funcionarioCpf text
    )
    """)

def postNota(notas):
    connection.execute("insert into nota (numero, data, subtotal, desconto, total, qntdProdutos, funcionarioCpf) values (?, ?, ?, ?, ?, ?, ?)", \
     (notas.numero, notas.data, notas.subtotal, notas.desconto, notas.total, notas.qntdProdutos, notas.funcionarioCpf ))
    connection.commit()

def deleteNota(numero):
    connection.execute("delete from nota where numero = ?", (numero,))
    connection.commit()

def updateNota(notas):
    connection.execute("update nota set data = ?, subtotal = ?, desconto = ?, total = ?, qntdProdutos = ?, funcionarioCpf = ? where numero = ?", \
     (notas.data, notas.subtotal, notas.desconto, notas.total, notas.qntdProdutos, notas.funcionarioCpf, notas.numero ))
    connection.commit()

def getNota():
    return connection.execute("select * from nota")    