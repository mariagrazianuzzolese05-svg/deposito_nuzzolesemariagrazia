#test 27-02
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datitest27-02.csv', sep='\t')


#guardando dal csv vediamo che ci sono dei doppioni
df = df.drop_duplicates()
df_cleaned = df.dropna()
print(df)

#ci sono delle case 'inivibili',mettiamo come range mq non inferiori a 40mq
df = df[df['Mq'] >= 40]
#creiamo una nuova colonna chiamata 'prezzo al mq'
df['Prezzo_al_Mq'] = df['Prezzo'] / df['Mq']
#calcoliamo medie e std per zone
media = df.groupby("Zona")["Prezzo"].mean()
mstd = df.groupby("Zona")["Prezzo"].std()

prezzo_massimo = df['Prezzo'].max()
prezzo_minimo = df['Prezzo'].min()
indice_massimo = df['Prezzo'].idxmax()
indice_minimo = df['Prezzo'].idxmin()
print(prezzo_massimo,indice_massimo)
print(prezzo_minimo,indice_minimo)

#scatter plot per far vedere come cambia il prezzo in base ai mq
sns.scatterplot(x=df['Mq'], y=df['Prezzo'], hue=df['Zona'], s=100)
plt.title('Relazione Mq e Prezzo')
plt.xlabel('Mq')
plt.ylabel('Prezzo')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

#grafico a barre per far vedere il prezzo in base alla zona
plt.figure(figsize=(10, 6))
sns.barplot(x="Zona", y="Prezzo", data=df, palette="magma", hue="Zona")
plt.title('Prezzo per Zona')
plt.xlabel('Zona')
plt.ylabel('Prezzo')
plt.show()