import referent

def header():
    print(" -------------------- ")
    print("|     Referente      |")
    print(" -------------------- ")

def inputReferente():
    return referent.Referente(
        input("Número da nota: "),
        input("Código do Produto: "),
        int(input("Quatidade: ")),
        float(input("Preço: ")),
        float(input("Desconto: "))
    )

def createReferente():
    referent.createTable()        
    
    ref = inputReferente()
    referent.postReferente(ref)
    
def getChanges():
    for r in referent.getReferente():
        print(r)

def deleteChange():
    ntn = input("Numéro da nota: ") 
    referent.deleteReferente(ntn)
    
def updateChange():
    ref = inputReferente()
    referent.updateReferente(ref)
    

if __name__ == "__main__":
    header()
    createReferente()
    getChanges()
    deleteChange()
    getChanges()
    updateChange()
    getChanges()