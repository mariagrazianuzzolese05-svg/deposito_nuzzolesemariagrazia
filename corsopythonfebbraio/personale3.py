'''Create un programma python utilizzando le api

https://pokeapi.co/api/v2/pokemon/ {numero} che simula un

pokedex, quando troverete un pokemon in maniera randomica

verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.

(Sul sistema API sono presenti poco più di 1000 pokemon)'''
import random
import requests
import json

#se il file esiste leggilo,sennò crea lista
def file():

    try:
        with open("filepokedex.json","r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError): 
        return[]

def incontrapokemon():
    pokemon=random.randint(1, 1025)
    url=f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    risposta=requests.get(url)
    dati = risposta.json()
    print("\n--- HAI INCONTRATO", dati['name'].upper(), "!---") # Stampa qui!
    return dati

    #print("Esperienza base:", dati['base_experience'])
    
    #print("Massa (hg):", dati['weight'])

    #print("Altezza (dm):", dati['height'])
#datiglobali=incontrapokemon()
def run():
    return 'sei scappato da',datiglobali['name']
def aggiungialpokedex():
    pokedex_attuale = file()
    if pokedex_attuale is None: # Protezione se file() non restituisce nulla
        pokedex_attuale = []
    nuovo_pokemon = {
        "nome": datiglobali['name'],
        "esperienza": datiglobali['base_experience'],
        "massa": datiglobali['weight'],
        "altezza": datiglobali['height']
    }
    pokedex_attuale.append(nuovo_pokemon)
    with open("filepokedex.json", "w") as file_json:
        json.dump(pokedex_attuale, file_json, indent=4)

    
def cattura():
    print('hai scelto cattura')
    catch=random.choice(["cattura riuscita", "cattura non riuscita"])
    if catch=='cattura riuscita':
        print('Preso! Aggiunto al pokedex.')
        return True
    else:
        print('Peccato, è scappato...')
        return False

def leggi_pokedex():
    elenco = file() # Prende la lista dal file JSON
    
    if not elenco:
        print("\nIl tuo Pokédex è vuoto. Vai a caccia!")
    else:
        print("\n--- I TUOI POKÉMON CATTURATI ---")
        for i, p in enumerate(elenco, 1):
            print(i, ".", p['nome'].upper(), "| Esp:", p['esperienza'], "| Massa:", p['massa'], "hg | Altezza:", p['altezza'], "dm")
        print("--------------------------------")



def main():
    print("--- POKEDEX ---")
    
    while True:
        global datiglobali
        datiglobali = incontrapokemon()
        scelta = input("\nCosa vuoi fare? (cattura / scappa / leggi / esci): ").lower()
        
        if scelta == "cattura":
            if cattura():
                aggiungialpokedex()
        elif scelta == "scappa":
            print(run())
        elif scelta == "leggi":
            leggi_pokedex()
        elif scelta == "esci":
            print("Salvataggio dati e chiusura...")
            break
main()
    