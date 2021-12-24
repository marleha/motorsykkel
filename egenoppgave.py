# Oppgave 5: Egen oppgave

# Oppgavetekst:
# Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal
# konstruktøren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot
# en tekststreng og legger den til i hobbyer-listen. Skriv også en metode skrivHobbyer.
# Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter
# Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på
# metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
# med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så
# mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
# statistikk om brukeren skrives ut.
 
# Kommentar:
#Først lages en klasse med klassenavnet Person. I konstruktøren eller instansmetoden blir 
#instansvariablene navn, alder og hobbyer med en tom liste definert. En metode leggTilHobbyer
#blir lagd, når bruker kaller på metoden blir teksten bruker skriver inn lagd inn i hobbyer listen. 
#En metoden skrivHobbyer blir lagd som printer hobbyer. En metode skrivUt lages hvor navn og alder
#printes og metoden skrivHobbyer kalles på og blir kjørt, hvor hobbyer blir printet ut. 

class Person:
    def __init__(self, navn, alder, hobbyer=[]):
        self._navn= navn
        self._alder= alder
        self._hobbyer= hobbyer

    def leggTilHobby(self,tekst):
        self._hobbyer = self._hobbyer.append(tekst)

    def skrivHobbyer(self):
        print("Hobbyene til personen er ", self._hobbyer)
    
    def skrivUt(self):
        print("Navnet er", self._navn, "og alderen er", self._alder)
        self.skrivHobbyer()

#Vi går ut av klassen og spør brukeren om navn og deretter alder til en person, og lagrer dem i hver sin variabel.
#En tom liste hobbyer blir laget, deretter variabelen svar. Mens svar ikke er exit, som er en while-løkke, skal
#bruker skrive hobby til personen, som lagres i listen hobbyer. Hvis bruker skriver exit printes en tom streng og
#programmet går ut av løkken. 

navn=input("Skriv inn navnet til en person: ")
alder=input("Skriv inn alder til denne personen: ")

hobbyer = []
svar=""
while svar !=  "exit":
    svar=input("Skriv inn en hobby til denne personen.  Hvis du er ferdig med å skrive inn hobbyer trykk exit. ")
    if svar =="exit":
        print("")
    else:
        hobbyer.append(svar)
   
#Et objekt personJegLagde blir lagd med klassen Person, som tar inn navn, alder og hobbyer brukeren skrev inn.
#Metoden skrivUt blir kalt på og printer navn og alder bruker skrev inn med tekst, metoden skrivHobbyer blir
#kalt på og printer hobbyene til denne personen brukeren har skrevet inn.

personenJegLagde = Person(navn, alder, hobbyer)
personenJegLagde.skrivUt()