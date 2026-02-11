'''classe MembroSquadra:

Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)

Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore

Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti

Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro.'''

'''classe MembroSquadra:
Attributi:
nome (stringa)
età (intero)

Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)'''
conteggiopuntiA=0
conteggiopuntiB=0
squadraA=[]
squadraB=[]
assistA=[]
assistB=[]
allenatiriA=[]
allenatiriB=[]

class MembroSquadra:
    def __init__(self,nome:str, eta:int):
        self.nome=nome
        self.eta=eta
    def descrizione(self):
        print('il membro della sqyadra si chiama',self.nome,'e ha',self.eta)
    def formasquadra(self):
        global squadraA, squadraB

        while True:
            F=input('creare squadra A o B')
            if F=='a':
                sq=input('chi vuoi nella squadraA')
                match sq:
                    case 'ballotelli':
                        squadraA.append(balotelli)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break
                    case 'barella':
                        squadraA.append(barella)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break

                    case 'buffon':
                        squadraA.append(buffon)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break
                            
                    case 'icardi':
                        squadraA.append(icardi)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break

                    case 'chiesa':
                        squadraA.append(chiesa)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break
                    case 'puffon':
                        squadraA.append(puffon)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraA)
                            break

            elif F=='b':
                sq=input('chi vuoi nella squadraB')
                match sq:
                    case 'ballotelli':
                        squadraB.append(balotelli)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                        break
                    case 'barella':
                        squadraB.append(barella)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                            break

                    case 'buffon':
                        squadraB.append(buffon)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                            break
                            
                    case 'icardi':
                        squadraB.append(icardi)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                            break

                    case 'chiesa':
                        squadraB.append(chiesa)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                            break
                    case 'puffon':
                        squadraB.append(puffon)
                        altro=input('altro?')
                        if altro=='no':
                            print(squadraB)
                            break
    

'''Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore'''

class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero):
        self.ruolo=ruolo
        self.numero=numero
        super().__init__(nome, eta)
    def descrizione(self):
        return super().descrizione()
    def gioca(self):
        print('inizia la partita')
        
    def rigore(self):
        global squadraA, squadraB
        print('rigore per infortunio e goal,un punto ad A')
        conteggiopuntiA+=1
        print(conteggiopuntiA)
    def infortunio(self):
        global squadraA, squadraB
    
        x=input('chi si infortunia?')
        match x:
            case 'balotelli':
                if balotelli in squadraA:
                    print('tutto ok')
                else:
                     conteggiopuntiB+=1
                     print('un punto a B')
            case 'buffon':
                if buffon in squadraA:
                    conteggiopuntiB+=1
                    print('ahia,pun punto a B')
                else:
                     conteggiopuntiB+=1
                     print('un punto a B')
                  
                  
            case _:
                  print('non cambia niente')
                
    def goal(self):
        global squadraA, squadraB
        t=input('uno dei giocatori tenta il goal,chi sarà?')
        match t:
             case 'ballotelli':
                  if balotelli in squadraA:
                    conteggiopuntiA+=1
                    print('goal per A')
                  else:
                     conteggiopuntiB+=1
                     print('un punto a B')
             case 'barella':
                  if barella in squadraA:
                    conteggiopuntiA+=1
                    print('goal per A')
                  else:
                     conteggiopuntiB+=1
                     print('un punto a B')
             case 'puffon':
                  print('puffon non conosce le regole del calcio misa')
             case 'buffon':
                  print('buffon non farebbe mai una cosa così')
             case 'chiesa':
                  if chiesa in squadraA:
                    conteggiopuntiA+=1
                    print('goal per A')
                  else:
                     conteggiopuntiB+=1
                     print('un punto a B')
             case _:
                  print('mancato')
        
    def parata(self):
         global squadraA, squadraB
         p=input('stanno per tirare un goal,chi parerà')
         match p:
              case 'buffon':
                   print('para')
              case 'puffon':
                   conteggiopunti -=1
                   print('perdono un punto',conteggiopunti)
              case _:
                   print('impossibile')
    def vincita(self):
         global squadraA, squadraB
         if conteggiopuntiA>conteggiopuntiB:
              print('squadra a vince')
         elif conteggiopuntiB>conteggiopuntiA:
              print('vince b')
         elif conteggiopuntiA==conteggiopuntiB:
              print('pareggio')
                   
                   
             
'''
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti'''
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta,anni_esperienza):
        self.anni_esperienza=anni_esperienza
        super().__init__(nome, eta)
    def dirige(self):
        global squadraA, squadraB
        if allegri in allenatiriA:
            print('lascia da soli i giocatori e perdono due punti')
            conteggiopuntiA -=2
        elif allegri in allenatiriB:
             print('lascia da soli i giocatori e perdono due punti')
             conteggiopuntiB-=2
             print(conteggiopuntiB)
        elif conte in allenatiriA:
            print('con la sua saggiezza fa fare due goal')
            conteggiopuntiA +=2
            print(conteggiopuntiA)
        elif conte in allenatiriB:
             print('lascia da soli i giocatori e perdono due punti')
             conteggiopuntiB-=2
             print(conteggiopuntiB)
    def all(self):
         while True:
            allena=input(('aggiungere a squadra A o B'))
            if allena=='a':
                 who=input('chi vuoi in a')
                 if who=='allegri':
                      allenatiriA.append(allegri)
                      altro=input('altro?')
                      if altro=='no':
                        print(squadraA)
                        break
                 elif who=='conte':
                      allenatiriA.append(conte)
                      altro=input('altro?')
                      if altro=='no':
                        print(squadraA)
                        break 
            elif allena=='b':   
                 if who=='allegri':
                      allenatiriB.append(allegri)
                      altro=input('altro?')
                      if altro=='no':
                        print(squadraA)
                        break
                 elif who=='conte':
                      allenatiriB.append(conte)
                      altro=input('altro?')
                      if altro=='no':
                        print(squadraA)
                        break           
        

'''Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team'''
class Assistente(MembroSquadra):
    def __init__(self, nome, eta,specializzazione):
        self.specializzazione=specializzazione
        super().__init__(nome, eta)
    def fisio(self):
        global squadraA, squadraB
        if doc in assistA:
            print('fa un massaggio ha tutti e fanno un goal')
            conteggiopuntiA +=1
            print(conteggiopuntiA)
        elif log in assistB:
            conteggiopuntiA +=1
            print('fa un massaggio ha tutti e fanno un goal')
            print(conteggiopuntiB)
        conteggiopunti +=1
        print(conteggiopunti)
    def analista(self):
        global squadraA, squadraB
        if log in assistA:
            print("'l'analista analizza male e fa perdere un punto")
            conteggiopuntiA -=1
            print(conteggiopuntiA)
        elif log in assistB:
            conteggiopuntiA -=1
            print(conteggiopuntiB)
            print("'l'analista analizza male e fa perdere un punto")
    def assist(self):
         while True:
            assist=input(('aggiungere a squadra A o B'))
            if assist=='a':
                 who=input('chi vuoi in a')
                 if who=='doc':
                      assistA.append(doc)
                      altro=input('altro?')
                      if altro=='no':
                        print('fatto')
                        break
                 elif who=='log':
                      assistA.append(log) 
                      altro=input('altro?')
                      if altro=='no':
                        print('fatto')
                        break 
            elif assist=='b':   
                 if who=='doc':
                      assistB.append(doc)
                      altro=input('altro?')
                      if altro=='no':
                        print('fatto')
                        break
                 elif who=='log':
                      assistB.append(log)
                      altro=input('altro?')
                      if altro=='no':
                        print('fatto')
                        break 
allegri=Allenatore('allegri',40,3)
conte=Allenatore('conte',54,10)

doc=Assistente('doc',33,'fisioterapista')
log=Assistente('log',22,'analista')

balotelli=Giocatore('balotelli',32,'attacante',11)
barella=Giocatore('barella',22,'difensore',33)
buffon=Giocatore('buffon',44,'portiere',23)

icardi=Giocatore('icardi',22,'attaccante',22)
chiesa=Giocatore('chiesa',25,'difensore',55)
puffon=Giocatore('puffon',29,'portiere',38)

def main():
     balotelli.formasquadra()
     conte.all()
     doc.assist()
     balotelli.gioca()
     balotelli.goal()
     balotelli.parata()
     doc.fisio()
     log.analista()
     balotelli.vincita()
main()






    

    