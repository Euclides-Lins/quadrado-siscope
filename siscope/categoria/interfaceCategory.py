import category

def header():
    print(" -------------------- ")
    print("|     Categoria      |")
    print(" -------------------- ")
    
def inputCategoria():
    return category.Categoria(                            
       int(input("Codigo: ")),                           
       input("Nome: "),                                  
       True if input("Ativo [S/n]: ")[0] in ("S", "s", "")else False  
    ) 

def createCategoria():
    category.createTable()
    
    cat =  inputCategoria()   
    category.postCategoria(cat)

def getChanges():
    for cat in category.getCategoria():
        print(cat)
        
def deleteChange():
    cod = int(input("Entre o codigo que desejas deletar :"))
    category.deleteCategoria(cod)
    
def updateChange():
    cat = inputCategoria()
    category.updateCategoria(cat)

if __name__ == "__main__":
    header()
    deleteChange()
    getChanges()