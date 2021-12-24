#Oppgave 4: Hund

#Først blir klassen Hund import fra filen hund.py. Deretter defineres prosedyren hovedprogram.
#Prosedyren kalles på og inni prosedyren lages et objekt Leo med klassen Hund, og egenskapene eller
#instansvariablene blir fylt ut. Man trenger ikke å fylle ut metthet, fordi den er allerede bestemt. 
# Deretter kalles spring på med Leo som objekt, den blir kjørt og etterpå blir vekten hentet og printet. 
# Dette skjer en gang til. Deretter blir spis metoden med Leo som objekt kalt på, med 100 som argument
#og Leos vekt blir hentet og prntet igjen. Dette skjer en gang til, bare med 200 som argument i spis
#metodekallet. 

from hund import Hund

def hovedprogram():
    Leo= Hund(2, 10)
    Leo.spring()
    print("Leo sin vekt er: ", Leo.HentVekt())
    Leo.spring()
    print("Leo sin vekt er: ", Leo.HentVekt())
    Leo.spis(100)
    print("Leo sin vekt er: ", Leo.HentVekt())
    Leo.spis(200)
    print("Leo sin vekt er: ", Leo.HentVekt())

hovedprogram()

