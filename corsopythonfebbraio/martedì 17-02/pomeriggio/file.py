def creafile():
    with open("csv.txt","r") as file:
        contenuto=file.read()
    print(contenuto)

def lines():
    with open("csv.txt","r") as file:
        contenuto=file.readlines()
    print(contenuto)

def scrivifile(stringa):  
    with open("csv2.txt","w") as file:
        file.write(stringa)



def aggiungi():  
    with open("csv2.txt","a")as file:
        file.write("ciao")
#matrice=[x.split(",")for x in #lista]
#matrice
matrice=[['nome','cognome','indirzzo'],
        ['tomaso','muraca','via roma'],
        ['giovanni','rossi','via milano'],
        ['teresa','verdi','via torino']]

for riga in range(1,len(matrice)):
    if matrice[riga][1]=="rossi":
       matrice[riga][1]='verdi'


       listac=[]
       for riga in matrice:
           listac.append(",".join(riga))
listac2=[",".join(x) for x in matrice]

stringaF= "\n".join(listac2)

scrivifile('abc')