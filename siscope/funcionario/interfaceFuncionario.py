import funcionario
class Funcionario:
    cpf = ''
    nome = ''
    email = ''
    senha = ''
    sexo = ''
    dataNascimento = ''
    funcao = ''
    fone = ''
    foto = ''
    dataInicio = ''
    dataSaida = ''
    historico = ''

def header():
    print(" -------------------- ")
    print("|     Funcionario    |")
    print(" -------------------- ")

def createFuncionario():
    funcionarios = Funcionario()
    funcionario.createTable()
    
    funcionarios.cpf = input("CPF :")
    funcionarios.nome = input("Nome :")
    funcionarios.email = input("EMail :")
    funcionarios.senha = input("Senha :")
    funcionarios.sexo = input("sexo :")
    funcionarios.dataNascimento = input("Data de Nascimento :")
    funcionarios.funcao = input("Funcao :")
    funcionarios.fone = input("Fone :")
    funcionarios.dataInicio = input("Data de Inicio :")
    funcionarios.dataSaida = input("Data de Saida :")
    funcionarios.historico = input("Historico:")
    
    funcionario.postFuncionario(funcionarios)

def getChanges():
    for func in funcionario.getFuncionario():
        print(func)

def deleteChange():
    cpf = input("Entre o cpf que desejas deletar :")
    funcionario.deleteFuncionario(cpf)

def updateChange():
    funcionarios = Funcionario()
    
    funcionarios.cpf = input("CPF :")
    funcionarios.nome = input("Nome :")
    funcionarios.email = input("EMail :")
    funcionarios.senha = input("Senha :")
    funcionarios.sexo = input("sexo :")
    funcionarios.dataNascimento = input("Data de Nascimento :")
    funcionarios.funcao = input("Funcao :")
    funcionarios.fone = input("Fone :")
    funcionarios.dataInicio = input("Data de Inicio :")
    funcionarios.dataSaida = input("Data de Saida :")
    funcionarios.historico = input("Historico:")

    funcionario.updateFuncionario(funcionarios)


header()
createFuncionario()
updateChange()
deleteChange()
getChanges()