#pd.to_datetime()

#Converte un indice o una colonna in formato datetime, permettendo di sfruttare
#tutte le funzionalità di time series DI python


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
# esempio: colonna “date” in stringhe → datetime
df['date'] = pd.date_range(start='2024-01-01', periods=len(df), freq='D')

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# oppure per creare un indice
df.set_index('date', inplace=True)
df.index = pd.to_datetime(df['date'])


df_weekly = df.resample('W').mean(numeric_only=True) # Calcola la media solo sulle colonne numeriche
df_monthly = df.resample('ME').sum(numeric_only=True)
#DataFrame.resample()

#Ridimensiona (aggregate o down/up-sample) la frequenza temporale dei dati,
#specificando l’intervallo desiderato (‘D’=day, ‘M’=month, ‘H’=hour, …).



# partendo da un DataFrame con indice DatetimeIndex:

df_daily = df.resample('D').mean()      # media giornaliera

df_monthly = df.resample('ME').sum()     # somma mensile