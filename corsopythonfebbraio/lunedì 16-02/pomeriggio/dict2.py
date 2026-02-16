'''Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10'''

diz = {'Giovanni': [7, 8], 'Alfredo': [9, 9],'Michela': [10, 10, 10]}

x=input('vuoi vedere la media?')
if x=='si':
    for nome,voti in diz.items():
        media=sum(voti)//len(voti)
        print(nome, media) 