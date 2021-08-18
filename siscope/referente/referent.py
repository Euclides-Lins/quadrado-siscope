import sqlite3

connection = sqlite3.connect("../list-siscope.db")

class Referente:
    def __init__(self, nota_num, prod_cod, qtd, preco, desconto):
        self.nota_num = nota_num
        self.prod_cod = prod_cod
        self.qtd      = qtd
        self.preco    = preco
        self.desconto = desconto
        
def createTable():
    cursor = connection.cursor()
    connection.execute("""
        create table if not exists referente(
           nota_num text primary key,
           prod_cod text,
           qtd integer,
           preco float,
           desconto float 
        )  
    """)

def postReferente(referente):
    connection.execute(
        "insert into referente (nota_num, prod_cod, qtd, preco, desconto) values (?, ?, ?, ?, ?)",
        (referente.nota_num, referente.prod_cod, referente.qtd, referente.preco, referente.desconto)
    )
    connection.commit()
    
def deleteReferente(nota_num):
    connection.execute("delete from referente where nota_num = ?", (nota_num,))
    connection.commit()
    
def updateReferente(referente):
    connection.execute(
        "update referente set prod_cod = ?, qtd = ?, preco = ?, desconto = ? where nota_num = ?",
        (referente.prod_cod, referente.qtd, referente.preco, referente.desconto, referente.nota_num)
    )
    connection.commit()
    
def getReferente():
    return connection.execute("select * from referente")