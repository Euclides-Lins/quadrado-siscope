import nota

class Notas:
    numero = ''
    data = ''
    subtotal = 0.0
    desconto = 0.0,
    total = 0.0
    qntdProdutos = 0
    funcionarioCpf = ''
    
def header():
    print(" -------------------- ")
    print("|        Notas       |")
    print(" -------------------- ")


def createNota():
    notas = Notas()
    nota.createTable()
    
    notas.numero = input("Numero :")
    notas.data = input("Data :")
    notas.subtotal = float(input("Subtotal :"))
    notas.desconto = float(input("desconto :"))
    notas.total = float(input("Total :"))
    notas.qntdProdutos = int(input("Quantidade :"))
    notas.funcionarioCpf = input("CPF do funcionario : ")
    nota.postNota(notas)

def getChanges():
    for grade in nota.getNota():
        print(grade)

def deleteChanges():
    num = input("Entre o numero que desejas deletar :")
    nota.deleteNota(num)

def updateChanges():
    notas = Notas()
    notas.numero = input("Numero :")
    notas.data = input("Data :")
    notas.subtotal = float(input("Subtotal :"))
    notas.desconto = float(input("desconto :"))
    notas.total = float(input("Total :"))
    notas.qntdProdutos = int(input("Quantidade :"))
    notas.funcionarioCpf = input("CPF do funcionario : ")
    nota.updateNota(notas)

header()
updateChanges()
getChanges()