'''#Series.shift()

#“Sposta” i valori lungo l’asse temporale di un numero di periodi, utile per
#calcolare differenze ritardate, tassi di crescita, ecc.


# aggiunge una colonna con il valore del giorno precedente

df['prev_day'] = df['value'].shift(1)

# tasso di variazione giornaliero

df['daily_return'] = df['value'].pct_change()  

# equivalente a shift + calcolo %


Series.rolling()

Calcola statistiche mobili su una finestra temporale scorrevole.


# finestra mobile di 7 giorni: media e deviazione standard

df['rolling_mean7'] = df['value'].rolling(window=7).mean()

df['rolling_std7']  = df['value'].rolling(window=7).std()'''