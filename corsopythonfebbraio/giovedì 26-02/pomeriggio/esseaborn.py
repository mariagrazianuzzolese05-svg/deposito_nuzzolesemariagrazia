'''Esercizio Medio: Normalizzazione dei Dati
Testo dell'esercizio:

Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 

Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.


Fornisci un codice che:

Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).

Applichi la normalizzazione min-max alle colonne altezza e peso.

Stampa sia il DataFrame originale sia quello modificato per compararli.'''
import pandas as pd

data = {
    'altezza': [160, 175, 182, 168, 190, 155],
    'peso': [55, 70, 85, 62, 95, 48],
    'età': [22, 25, 30, 28, 35, 21]
}
df = pd.DataFrame(data)

#formula: (valore - minimo) / (massimo - minimo)
df['altezza_Norm'] = (df['altezza'] - df['altezza'].min()) / (df['altezza'].max() - df['altezza'].min())
df['peso_Norm'] = (df['peso'] - df['peso'].min()) / (df['peso'].max() - df['peso'].min())

dfmodificato=pd.DataFrame(df['altezza_Norm'],df['peso_Norm'],df['età'])
#rint(df)
print(dfmodificato)