#Oppgave 2: Motorsykkel

#Først lages en klasse med klassenavnet Motorstykkel. I konstruktøren eller instansmetoden blir instansvariabelene
#merke, registreringsnummer og kilometerstand definert. En metode kjor blir lagd hvor bruker kan
#øke kilometerstanden ved å velge km. Km blir addet med kilometerstand. En metode hentKilometerstand 
# blir definert hvor kilometerstand blir returnert til metodekallet. En metode skrivUt blir definert
#hvor alle intansvariablene blir printet.

class Motorsykkel:
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self._merke= merke 
        self._registreringsnummer= registreringsnummer
        self._kilometerstand=kilometerstand

    def kjor(self,km):
        self._kilometerstand= self._kilometerstand + km

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print(self._merke, self._registreringsnummer, self._kilometerstand)

