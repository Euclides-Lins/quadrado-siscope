import product
class Produto:
    codigo = ''
    nome = ''
    descricao = ''
    preco = 0.0
    desconto = 0.0
    quantidade = 1

def header():
    print(" -------------------- ")
    print("|      Produto       |")
    print(" -------------------- ")

def createProduto():
    produto = Produto()
    product.createTable()
    
    produto.codigo = input("Codigo :")
    produto.nome = input("Nome :")
    produto.descricao = input("Descricao :")
    produto.preco = float(input("Preco :"))
    produto.desconto = float(input("Desconto :"))
    produto.quantidade = int(input("Quantidade :"))
    product.postProduto(produto)

def getChanges():
    for prod in product.getProduto():
        print(prod)

def deleteChange():
    cod = input("Entre o codigo que desejas deletar :")
    product.deleteProduto(cod)

def updateChange():
    produto = Produto()
    produto.codigo = input("Codigo :")
    produto.nome = input("Nome :")
    produto.descricao = input("Descricao :")
    produto.preco = float(input("Preco :"))
    produto.desconto = float(input("Desconto :"))
    produto.quantidade = int(input("Quantidade :"))
    product.updateProduto(produto)


if __name__ == "__main__":
    header()
    getChanges()
    createProduto()
    updateChange()
    getChanges()