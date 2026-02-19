'''{
    'nome':'tommaso',
    'cognome':'muraca'

 }'''

'''come leggere json? bisogna importare json'''
import json

x = '{"nome":"tommaso","cognome":"muraca"}'

'''json load converte x in dict'''

#diz =json.load(diz, type{diz})

dizMy ={"nome":"tommaso"}
#jsonNew =json.dumps(dizMy,indent=4,sep=(",","="),sort_keys=True)
#print(type(jsonNew),"\n",jsonNew)

#come fare richieste api
import requests
risposta= requests.get("https://www.google.com/")
print(risposta)
print(risposta.text) #dà codice httml google

url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&forecast_days=1"
risposta=requests.get(url)
JsonS =risposta.text
JsonDiz =json.load(JsonS)
print(JsonDiz["hourly"]["time"][0]) #per avere dati 
previsioni =JsonDiz["hourly"]
for i in range(len(previsioni["time"])):
    print(f"giorno{ previsioni["time"][i]}temperatira:{ previsioni["temperature_2m"][i]}")
JsonDiz =risposta.json()
#al posto di importare
''' a berlino mettere tra graffe city che è la variabile di input https://geocoding-api.open-meteo.com/v1/search?name=Berlino&count=1&language=it&format=json'''
