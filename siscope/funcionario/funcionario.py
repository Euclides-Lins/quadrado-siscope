import sqlite3

connection = sqlite3.connect("../list-siscope.db")

def createTable():
    cursor = connection.cursor();
    connection.execute("""
    create table if not exists funcionario (
        cpf text,
        nome text,
        email text,
        senha text,
        sexo text,
        dataNascimento text,
        funcao text,
        fone text,
        foto text,
        dataInicio text,
        dataSaida text,
        historico text
    )
    """)

def postFuncionario(funcionario):
    connection.execute("insert into funcionario (cpf, nome, email, senha, sexo, dataNascimento, funcao, fone, dataInicio, dataSaida, historico) values (?,?, ?,?,?,?,?,?,?,?,?)", \
     (funcionario.cpf, funcionario.nome, funcionario.email, funcionario.senha, funcionario.sexo, funcionario.dataNascimento, funcionario.funcao, funcionario.fone, funcionario.dataInicio, funcionario.dataSaida, funcionario.historico ))
    connection.commit()

def deleteFuncionario(cpf):
    connection.execute("delete from funcionario where cpf = ?", (cpf,))
    connection.commit()

def updateFuncionario(funcionario):
    connection.execute("update funcionario set nome = ?, email = ?, senha = ?, sexo = ?, dataNascimento = ?, funcao = ?, fone = ?,  dataInicio = ?, dataSaida = ?, historico = ?  where cpf = ?", \
     (funcionario.nome, funcionario.email, funcionario.senha, funcionario.sexo, funcionario.dataNascimento, funcionario.funcao, funcionario.fone, funcionario.dataInicio, funcionario.dataSaida, funcionario.historico, funcionario.cpf ))
    connection.commit()

def getFuncionario():
    return connection.execute("select * from funcionario")    