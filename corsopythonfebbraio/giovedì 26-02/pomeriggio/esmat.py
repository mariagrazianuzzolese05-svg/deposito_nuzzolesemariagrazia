'''Esercizio Facile: Calcolo di Statistiche di Base


Testo dell'esercizio:

Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese. 


Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:

La temperatura massima

La temperatura minima

La temperatura media

La mediana delle temperature'''
import pandas as pd
import matplotlib.pyplot as plt

dataset_temperature = {
    "temperature": [
        15.9, 14.1, 16.3, 18.8, 13.8, 13.8, 18.9, 16.6, 13.2, 16.0,
        13.2, 13.2, 15.2, 9.1, 9.7, 12.9, 11.7, 15.4, 12.0, 10.5,
        18.6, 13.9, 14.7, 10.5, 13.0, 14.8, 11.3, 15.6, 12.8, 13.7
    ]
}

df = pd.DataFrame(dataset_temperature)

temperatura_massima=df['temperature'].max()
giorno_del_massimo = df['temperature'].idxmax()

temperatura_minima=df['temperature'].min()
giorno_del_minimo = df['temperature'].idxmin()

temperatura_media=df['temperature'].mean()
temperatura_mediana=df['temperature'].median()


plt.figure()
#plt.plot(df['temperature'], marker='o', color='blue')
plt.plot(df['temperature'], marker='*', color='green')
plt.axhline(temperatura_massima, color='red', linestyle='--', alpha=0.6, label=f'Max: {temperatura_massima}°C')
plt.axhline(temperatura_minima, color='blue', linestyle='-.', alpha=0.6, label=f'Min: {temperatura_minima}°C')
plt.axhline(temperatura_media, color='orange', linestyle='-', label=f'Media: {temperatura_media}°C')
plt.axhline(temperatura_mediana, color='green', linestyle=':', label=f'Mediana: {temperatura_mediana}°C')
# Evidenziamo il punto di massimo con uno scatter rosso sopra la tua stella verde
plt.scatter(giorno_del_massimo,temperatura_massima, color='red', s=150, zorder=5, label='Picco del Mese')
plt.scatter(giorno_del_minimo,temperatura_minima, color='blue', s=150, zorder=5, label='contrario del picco del Mese')
plt.title('Andamento Temperature')
plt.xlabel('Giorno del Mese')
plt.ylabel('Gradi Celsius (°C)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), shadow=True, title="Legenda Termica")
plt.tight_layout()
#plt.grid(True)
plt.show()



plt.figure()
#plt.hist(df['temperature'], bins=30)
plt.hist(df['temperature'], bins=5)
plt.title('Istogramma temperature')
plt.xlabel('giorni')
plt.ylabel('temperature')
plt.show()

giorni=30

'''plt.figure()
plt.bar(giorni,df['temperature'])
plt.title('Grafico a Barre T')
plt.xlabel('giorni')
plt.ylabel('T')
plt.show()'''

