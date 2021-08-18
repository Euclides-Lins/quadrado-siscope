import product

def header():
    print(" -------------------- ")
    print("|      Produto       |")
    print(" -------------------- ")

def test():
    product.createTable()
    product.getProduto()


header()
test()