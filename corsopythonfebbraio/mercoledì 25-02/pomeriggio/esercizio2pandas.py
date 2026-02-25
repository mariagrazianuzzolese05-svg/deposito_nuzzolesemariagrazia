'''Esercizio 2: Manipolazione e Aggregazione dei Dati
Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

Caricare i dati in un DataFrame.
Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
Trovare il prodotto più venduto in termini di Quantità.
Identificare la città con il maggior volume di vendite totali.
Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
Visualizzare il numero di vendite per ogni città.
'''
import pandas as pd
df = pd.read_csv('analisivendite.csv')

'''dataset_vendite = {
    "Prodotto": ["Laptop", "Mouse", "Monitor", "Tastiera", "Laptop", "Mouse"],
    "Quantità": [5, 12, 7, 10, 3, 15],
    "Prezzo Unitario": [1200.00, 25.50, 200.00, 45.00, 1200.00, 25.50],
    "Città": ["Bari", "Milano", "Roma", "Bari", "Roma", "Milano"]
}
df = pd.DataFrame(dataset_vendite)'''
df['Totale Vendite'] = df['Quantità']*df['Prezzo Unitario']

print('totale vendite')
print(df['Totale Vendite'] )
print('---totale vendite---')

quantita_per_prodotto=df.groupby('Prodotto')['Totale Vendite'].sum()
valore_max = quantita_per_prodotto.max()
quantita_per_citta=df.groupby('Città')['Totale Vendite'].sum()
citta = quantita_per_citta.max()

print('valore max prodotto')
print(valore_max)
print('----valore max prodotto----')

print('quantita per prodotto')
print(quantita_per_prodotto)
print('----quantita per prodotto----')

print('max città')
print(citta)
print('---max città---')

df_vednite = df[df['Totale Vendite'] > 1000]
print('vendite sup 1000')
print(df_vednite)
print('---vendite sup 1000---')

df_ordinato = df.sort_values(by='Totale Vendite', ascending=False)
#frequenza_citta = df['Città'].value_counts()
conteggio_citta = df.groupby('Città')['Prodotto'].count()
print('conteggio città')
print(conteggio_citta)
print('---conteggio città---')

print('df')
print(df)
print('---df---')

df.to_csv('vendite_elaborate.csv', index=False)