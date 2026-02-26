# Generazione di una serie di date
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


date_range = pd.date_range(start='2021-01-01',
periods=10, freq='ME')
df.index = date_range

date_2024 = pd.date_range(start='2026-01-01', end='2026-12-31')
# Resampling dei dati di una serie temporale

df_resampled = df.resample('ME').mean()