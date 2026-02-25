'''Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario.

Caricare i dati in un DataFrame autogenerandoli casualmente .
Visualizzare le prime e le ultime cinque righe del DataFrame.
Visualizzare il tipo di dati di ciascuna colonna.
Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
Identificare e rimuovere eventuali duplicati.
Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
Salvare il DataFrame pulito in un nuovo file CSV.
'''
import pandas as pd
dataset_persone = {
    "Nome": ["Marco", "Anna", "Luca", "Giulia", "Matteo", "Elena", "Sandro", "Sofia", "Ciccio", "Chiara", 
             "Paolo", "Lucia", "Piero", "Sara", "Enzo", "Rita", "Leo", "Gaia", "Vito", "Ilaria"],
    
    "Età": [24, 31, 45, 22, 56, 29, 38, 50, 19, 42, 
            33, 27, 6, 77, 48, 26, 53, 21, 40, 30],
    
    "Città": ["Bari", "Milano", "Roma", "Napoli", "Torino", "Bari", "Milano", "Roma", "Napoli", "Bari",
              "Torino", "Milano", "Roma", "Bari", "Napoli", "Torino", "Milano", "Roma", "Bari", "Napoli"],
    
    "Salario": [1850.50, 2400.00, 3100.25, 1250.00, 4200.80, 2100.00, 2850.40, 3900.00, 1100.60, 3300.00,
                2600.15, 2250.00, 4450.90, 2700.00, 3050.30, 1950.00, 4100.20, 1400.00, 2950.75, 2300.00]
}
df = pd.DataFrame(dataset_persone)
print(df.head())
print('----------')
print(df.tail(5))
print('----------')
print(df.dtypes)
#statistiche = df[['Età', 'Salario']].describe()
#print(statistiche)
# Calcolo puntuale per il Salario
media_salario = df['Salario'].mean()
mediana_salario = df['Salario'].median()
std_salario = df['Salario'].std()
media_eta = df['Età'].mean()
mediana_eta = df['Età'].median()
std_eta= df['Età'].std()
print('Media:',media_salario)
print('Mediana:',mediana_salario)
print('Deviazione Standard:',std_salario)
print('Media:',media_eta)
print('Mediana:',mediana_eta)
print('Deviazione Standard:',std_eta)
df = df.drop_duplicates()
df_cleaned = df.dropna()
#df['Età'] = df['Età'].fillna(df['Età'].median())
#df['Salario'] = df['Salario'].fillna(df['Salario'].median())
df['Età'].fillna(df['Età'].median(), inplace=True)
df['Salario'].fillna(df['Salario'].median(), inplace=True)
#df_senior = df[df['Età'] > 65]
#df_adult = df[df['Età'].between(19, 65)]
#df_giovane = df[df['Età'] <= 18]
'''df['senior'] = df['Età'] > 65
df['adult'] = df['Età'].between(19, 65)
df['giovane'] = df['Età'] <= 18'''
df['Categoria Età'] = df['Età'].apply(lambda x: "Giovane" if x <= 18 else ("Adulto" if x <= 65 else "Senior"))
'''def categoria_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"'''
'''# 1. Aggiunta della colonna "Categoria Età"
# Definiamo i limiti: 0-18 (Giovane), 18-65 (Adulto), 65-120 (Senior)
intervalli = [0, 18, 65, 120]
etichette = ["Giovane", "Adulto", "Senior"]

df['Categoria Età'] = pd.cut(df['Età'], bins=intervalli, labels=etichette)'''

#df["Categoria Età"] = df["Età"].apply(categoria_eta)
df.to_csv('dataset_finito.csv', index=False)
print(df)
