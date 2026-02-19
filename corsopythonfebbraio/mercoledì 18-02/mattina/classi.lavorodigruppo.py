'''
Trasformare il programma che abbiamo creato in precedenza per la gestione dei voti degli alunni in un programma per la gestione di una classe che utilizza un file come database:
    All'avvio il programma chiede se si vuole leggere l'elenco degli alunni e i loro voti e medie, se si vuole aggiungere un alunno o un voto.

# In collaborazione con Elisabetta Carella e Mariagrazia Nuzzolese
'''

NOME_FILE = "voti.csv"


def scriviFile(nome_file, diz_studenti):
    stringa_totale = convertiDictToStr(diz_studenti)
    with open(nome_file, "w") as file:
        file.write(stringa_totale)


def leggFile(nome_file):
    with open(nome_file, "r") as file:
        contenuto = file.read()
    dizionario_totale = convertiStrToDict(contenuto)
    return dizionario_totale


def convertiDictToStr(dizionario):
    strg = ""                                   #Stringa
    for chiave, valore in dizionario.items():
        strg += f"{chiave},{'-'.join(map(str, valore))}\n" # "-".join(valore) = "-".join(map(str, valore))
    #print(strg.strip("\n"))
    return strg.strip("\n")


def convertiStrToDict(stringa):
    diz = {}
    lista_strg = stringa.split("\n")            #Stringa
    for riga in lista_strg:
        parti = riga.split(",")                     #Stringa
        chiave = parti[0]                           #Stringa
        valore = parti[1]                           #Stringa
        elementi = valore.split("-")                #Lista di Stringhe Numeriche
        numeri = list(map(int, elementi))           #Lista di Interi
        diz[chiave] = numeri
    #print(diz)
    return diz


# MAIN
studenti = {}

'''
try:
    with open(f"{NOME_FILE}", "r") as file:
        studenti = file.read()
        convertiDictToStr(stu)
except FileNotFoundError:
    print("Errore, file non trovato!")
'''
while True:
    print("Menu")
    print("1. Aggiungi Alunno")
    print("2. Aggiungi Voto")
    print("3. Stampa Studenti e Medie")
    scelta = input("Cosa vuoi fare? ")

    match scelta:
        case "1":
            if type(studenti) == str:
                studenti = convertiStrToDict(studenti)
            while True:
                nome = input("Inserisci studente: ").lower()
                if nome not in studenti.keys():
                    print("Studente Inserito!")
                    break
                print("Studente già presente!")
            studenti[nome] = []
            scriviFile(NOME_FILE, studenti)
        case "2":
            if type(studenti) == str:
                studenti = convertiStrToDict(studenti)
            nome = input("Inserisci studente: ").lower()
            if nome in studenti.keys():
                voto = input("Inserisci il voto: ")
                if len(studenti[nome]) == 0:
                    studenti[nome] = [voto]
                else:
                    studenti[nome].append(voto)
                scriviFile(NOME_FILE, studenti)
                print("Voto Inserito!")
            else:
                print("Studente non in elenco!")
        case "3":
            studenti = leggFile(NOME_FILE)
            if len(studenti) != 0:
                for nome in studenti.keys():       
                    if len(studenti[nome]) > 0:
                        media = sum(studenti[nome]) / len(studenti[nome])
                        print(f"Nome: {nome}, Media: {media}")
                    else:
                        print(f"Nome: {nome}, Nessun voto inserito")
                    break
            else:
                print("Nessuno studente trovato!")
            if type(studenti) == dict:
                studenti = convertiDictToStr(studenti)
        case _:
            print("Input Errato")
    print("")



studenti = {}

while True:
    nome_studente = input('Inserisci un nome o "media" per ottenere la media dei voti: ').lower()
    
    if nome_studente == 'media':
        break
    
    if nome_studente not in studenti:  # Uguale a dire studenti.keys() perché sottointeso
        studenti[nome_studente] = {}
        
        while True:
            nome_materia = input('Inserisci una materia o "stop" per uscire: ').lower()
            
            if nome_materia == 'stop':
                break
            
            if nome_materia not in studenti[nome_studente]:
                studenti[nome_studente][nome_materia] = []
                
                while True:
                    voto = input('Inserisci il voto o "stop" per uscire: ')
                    
                    if voto == 'stop':
                        break
                    
                    studenti[nome_studente][nome_materia].append(float(voto))
            
            else:
                print('Materia presente!')

    else:
        print('Studente già presente!')

'''
studenti = {
    'gabriele': {'scienze': [2.0], 'matematica': [5.0, 9.0]}, 
    'alessio': {'inglese': [5.0, 10.0]}
}
'''

for nome, valore in studenti.items():
    lista_voti = []
    
    for voti in valore.values():
        lista_voti.extend(voti)
    
    if len(lista_voti) > 0:
        media = sum(lista_voti) / len(lista_voti)
        print(f"Nome: {nome}, Media: {media}")
    else:
        print(f"Nome: {nome}, Nessun voto inserito")