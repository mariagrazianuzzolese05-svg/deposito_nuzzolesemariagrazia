#dizionari
student={
    "nome":"alice",
    "eta":20,
    "sesso":"femmina"
    }
student["eta"]=21
student["citta"]="roma"
print(student)
print(student["nome"])
print(student.keys())
print(student.values())

#for
'''def  stampapersona:
    print("\n--- Persona ---")
    for k, v in p.items():
        print(k.capitalize(), ":", v)

stampa_persona(persona)

#not
if "nome" in persona:
    print("\nLa chiave 'nome' esiste")

if "telefono" not in persona:
    print("La chiave 'telefono' NON esiste")'''

#dict di dict
'''self.catalogo = {
            "carta": {"prezzo": 5, "quantita": 10},
            "penna": {"prezzo": 1, "quantita": 20}}'''
#aggiungere
'''self.catalogo[x] = {"prezzo": y, "quantita": z}'''

#rimuovi
'''del self.catalogo[x]'''

#aggiorna
'''self.catalogo["articolo"]=p'''

#calcoli
'''qt=int(input('quanti ne vuoi'))
           prezzotot=negoz.catalogo[scelta]["prezzo"]*qt'''