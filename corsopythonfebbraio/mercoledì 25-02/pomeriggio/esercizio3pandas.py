'''Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.


Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.


Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.

Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.

Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto.'''

import pandas as pd
import numpy as np

citta = ["Bari", "Milano", "Roma"]
prodotti = ["Elettronica", "Abbigliamento", "Casa"]
giorni = np.arange(1, 31) 
dati = [(g, c, p) for g in giorni for c in citta for p in prodotti]
df = pd.DataFrame(dati, columns=["Data", "Città", "Prodotto"])

df["Vendite"] = np.random.uniform(50, 500, size=len(df))
print(df)

pivot_vendite = df.pivot_table(index="Città",columns="Prodotto", values="Vendite",  aggfunc="mean")
print(pivot_vendite)
venditetotali_per_prodotto=df.groupby('Prodotto')['Vendite'].sum()
print(venditetotali_per_prodotto)
