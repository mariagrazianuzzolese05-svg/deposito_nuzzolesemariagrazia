"""Create un programma python che permette tramite le api di visualizzare le previsione
metereologiche della città scelta dall'utente.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se
visionare oltre che le temperature anche la velocità del vento e le
probabili precipitazioni."""
import requests
import json
import time

city=input('inserisci città')
durata=int(input('(1)per leggere le previsioni di domani,\n(3)fra tre giorni,\n(7)fra sette giorni '))
var=input('altre variabili (vento/pioggia)? (si/no): ')

print(f"--- PREVISIONI PER {city.upper()} ---")
print("Caricamento dati in corso...")
time.sleep(1)


url=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=it"

risposta=requests.get(url)
diz = risposta.json()
dizm = json.dumps(diz, indent=4, sort_keys=True)
        #print(dizm)
lang=diz['results'][0]['latitude']
long=diz['results'][0]['longitude']
        #temp=diz['daily']


url2=f"https://api.open-meteo.com/v1/forecast?latitude={lang}&longitude={long}&hourly=temperature_2m,wind_speed_10m,precipitation_probability&timezone=auto&forecast_days={durata}"
rispostas=requests.get(url2)
diz2 = rispostas.json()
dizm2 = json.dumps(diz2, indent=4, sort_keys=True)
temp=diz2['hourly']['temperature_2m']
prec=diz2['hourly']['precipitation_probability']
wind=diz2['hourly']['wind_speed_10m']
ore = diz2['hourly']['time']
try:
    if var=='si':
        url=f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=it"

        risposta=requests.get(url)
        diz = risposta.json()
        dizm = json.dumps(diz, indent=4, sort_keys=True)
        #print(dizm)
        lang=diz['results'][0]['latitude']
        long=diz['results'][0]['longitude']
        #temp=diz['daily']

        print('attendere,previsioni per',city,'in corso')
        time.sleep(2)

        url2=f"https://api.open-meteo.com/v1/forecast?latitude={lang}&longitude={long}&hourly=temperature_2m,wind_speed_10m,precipitation_probability&timezone=auto&forecast_days={durata}"
        rispostas=requests.get(url2)
        diz2 = rispostas.json()
        dizm2 = json.dumps(diz2, indent=4, sort_keys=True)
        temp=diz2['hourly']['temperature_2m']
        prec=diz2['hourly']['precipitation_probability']
        wind=diz2['hourly']['wind_speed_10m']
        ore = diz2['hourly']['time']
       
        for i in range(len(ore)):
            print(f"Ora: {ore[i]} | Temp: {temp[i]}°C | Pioggia: {prec[i]}% | Vento: {wind[i]}km/h")
        print('-------fine programma-------')

    elif var=='no':
        print('stai per vedere previsioni senza le precipitazioni e velocità del vento')
        url3=f"https://api.open-meteo.com/v1/forecast?latitude={lang}2&longitude={long}&current=temperature_2m&timezone=auto&forecast_days={durata}"
        for i in range(len(ore)):
            print(f"Ora: {ore[i]} | Temp: {temp[i]}°C ")
        print('-------fine programma-------')

except:
    print('errore')

