#Oppgave 2: Motorsykkel

#Først blir klassen Motorsykkel import fra filen motorsykkel.py. Deretter defineres prosedyren hovedprogram.
#Prosedyren kalles på og inni prosedyren lages et objekt med klassen motorsykkel, og egenskapene eller
#instansvariablene blir fylt ut. To objekter til blir definert. Deretter bes det første objektet å bli
#skrevet ut, ved å kalle på metoden skrivUt som blir kjørt. Dette skjer med de to andre objektene også.
#Hos det siste objektet blir kilometerstand økt med 10 km, når metoden kjor blir kalt på og kjørt. Deretter
#kalles hentKilometerstand metoden på, til det siste objektet, hvor kilometerstand blir returnert til 
#metodekallet. Deretter kalles det på skrivUt metoden til det siste objektet. Der blir alle egenskapene til
#instansvariabelene skrevet ut når metoden blir kjørt.


from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykkelA= Motorsykkel("BMW", "ABC 786", 100)
    motorsykkelB= Motorsykkel("Toyota", "MLB 743", 200)
    motorsykkelC= Motorsykkel("Mercedes", "AB 12345", 300)
    motorsykkelA.skrivUt()
    motorsykkelB.skrivUt()
    motorsykkelC.skrivUt()
    motorsykkelC.kjor(10)
    motorsykkelC.hentKilometerstand()
    motorsykkelC.skrivUt()

hovedprogram()