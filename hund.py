#Oppgave 4: Hund

#Først lages en klasse med klassenavnet Hund. I konstruktøren eller instansmetoden blir instansvariablene alder, 
#vekt og metthet, som settes til å være 10, definert. En metode hentAlder blir lagd hvor alder
#blir returnert til metodekallet. En metode Hentvekt blir lagd hvor vekt blir også returnert
#til metodekallet. En metode spring blir lagd hvor hver gang den kalles trekkes metthet med 1. 
#Hvis metthet er mindre enn 5, trekkes vekt med 1. En metode spis blir lagd. Når den kalles blir
#metthet økt med 1. Hvis metthet er over 7, øker vekt med 1. 

class Hund:
    def __init__(self, alder, vekt, metthet=10):
        self._alder= alder
        self._vekt= vekt
        self._metthet= metthet

    def hentAlder(self):
        return self._alder

    def HentVekt(self):
        return self._vekt

    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self, heltall):
        self._metthet += heltall
        if self._metthet > 7:
            self._vekt += 1
