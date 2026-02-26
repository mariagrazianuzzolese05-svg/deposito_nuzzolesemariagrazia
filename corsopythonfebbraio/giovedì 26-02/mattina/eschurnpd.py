'''Obiettivo: Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.


Dataset: 

ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)


Caricamento e Esplorazione Iniziale:

Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.

Pulizia dei Dati:

Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

Analisi Esplorativa dei Dati (EDA):

Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.

Preparazione dei Dati per la Modellazione:

Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.

Analisi Statistica e Predittiva:

Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).'''

import pandas as pd

df = pd.read_csv('churn.csv')

print(df.info())
print(df.describe())
print(df.value_counts())


df = df.drop_duplicates()
#df_cleaned = df.dropna()

df['Tariffa_Mensile'] = df['Tariffa_Mensile'].fillna(df['Tariffa_Mensile'].median()) # Più robusto della media
df['Dati_Consumati'] = df['Dati_Consumati'].fillna(0) # Ipotesi fisica di inattività
df['Servizio_Clienti_Contatti'] = df['Servizio_Clienti_Contatti'].fillna(df['Servizio_Clienti_Contatti'].mode()[0])
#nella moda co zero indichiamo la prima moda che abbiamo visto che pottrebbero essercenen di più

# Teniamo solo le tariffe sotto i 200 euro (limite di ragionevolezza)
df = df[df['Tariffa_Mensile'] <= 200]

df['Eta'] = df['Eta'].abs()

df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
#per gestire infiniti(divisiome)
#df['Costo_per_GB'] = df['Costo_per_GB'].replace([np.inf, -np.inf], 0)

relazione_churn = df.groupby('Churn')[['Eta', 'Durata_Abbonamento', 'Tariffa_Mensile']].mean()
print(relazione_churn)

'''Prima di calcolare la correlazione, dobbiamo assicurarci che tutte le variabili siano numeriche. 
Poiché la colonna Churn contiene "Sì/No", dobbiamo convertirla in $1/0$ (come uno stato di spin o un bit binario)'''
'''Ottima domanda. Inserire Churn_Num nella matrice di correlazione è l'unico modo per rispondere alla
domanda fondamentale del tuo esercizio: "Cosa causa l'abbandono dei clienti?"'''
# Convertiamo il Churn in valori numerici per poterlo includere nella matrice
df['Churn_Num'] = df['Churn'].apply(lambda x: 1 if x == 'Si' else 0)
colonne_numeriche = ['Eta', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Churn_Num']
#colonne_numeriche = ['Eta', 'Durata_Abbonamento', 'Tariffa_Mensile']
matrice_corr = df[colonne_numeriche].corr()
print(matrice_corr)
print(df)






#normalizziamo tutto $$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$$
'''df['Eta_Norm'] = (df['Eta'] - df['Eta'].min()) / (df['Eta'].max() - df['Eta'].min())
df['Durata_Abbonamento_Norm'] = (df['Durata_Abbonamento'] - df['Durata_Abbonamento'].min()) / (df['Durata_Abbonamento'].max() - df['Durata_Abbonamento'].min())
df['Tariffa_Mensile_Norm'] = (df['Tariffa_Mensile'] - df['Tariffa_Mensile'].min()) / (df['Tariffa_Mensile'].max() - df['Tariffa_Mensile'].min())
df['Dati_Consumati_Norm'] = (df['Dati_Consumati'] - df['Dati_Consumati'].min()) / (df['Dati_Consumati'].max() - df['Dati_Consumati'].min())
df['Servizio_Clienti_Contatti_Norm'] = (df['Servizio_Clienti_Contatti'] - df['Servizio_Clienti_Contatti'].min()) / (df['Servizio_Clienti_Contatti'].max() - df['Servizio_Clienti_Contatti'].min())
df['Costo_per_GB_Norm'] = (df['Costo_per_GB'] - df['Costo_per_GB'].min()) / (df['Costo_per_GB'].max() - df['Costo_per_GB'].min())'''



