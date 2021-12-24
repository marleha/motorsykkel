#Oppgave 1: Salgsstatistikk

#Først oppretter jeg en ordbok, deretter definerer en funksjon. Funksjonen blir kalt på med filens navn som argument.
#Inni funksjonen lagres filen i minfil variabelen. For løkken går gjennom hver linje i filen og splitter den for
#hver bit på hver linje. De første bitene på hver linje lagres i navn variabelen, og de andre bitene på hver linje
#lagres i verdi. navn og verdi blir lagt inn i ordbok, og ordboken blir returnert til funksjonskallet. 

#1
ordbok= {}

def innlesing(filnavn):
    minfil=open(filnavn)
    for linje in minfil:
        biter=linje.split()
        navn=biter[0]
        verdi=int(biter[1])
        ordbok[navn]= verdi
    return ordbok

ordbok=innlesing("lesfil.txt")

#SPØR
#Først definerer jeg en prosedyre med ordbok som argument. Prosedyren blir kalt på med ordbok som argument. Inni prosedyren settes en variabel
#storst til å være 0. En for-løkke går gjennom hver verdi i ordbok og finner største verdi, deretter printes den største verdien med tekst.
#2
def maanedensSalgsperson(parameter1):
    storst=0
    for navn,verdi in parameter1.items():
        if verdi > storst:
            storst=verdi
            ansatt=navn
    print("Maanedens ansatte er",ansatt, "med", storst,"salg.")

maanedensSalgsperson(ordbok)

#Først definerer jeg en funksjon og deretter kaller på funksjonen med ordbok som argument. Inni funksjonen settes tall variabelen for å være
#0. I for løkken går programmet gjennom hver verdi i ordboken og summerere dem sammen og lagres i variabelen tall, som returneres til
#der funksjonen ble kalt på. Returverdier lagres i en ny variabel som printes sammen med tekst. 
#3
def totalAntallSalg(parameter1):
    tall=0
    for navn,verdi in parameter1.items():
        nummer=int(verdi)
        tall= tall + nummer
    return tall

antall_sum= totalAntallSalg(ordbok)
print("Totalt antall salg:", antall_sum)

#Først definerer jeg en funksjon og deretter kalles funksjonen på med argument ordbok. Inni funksjonen settes tall variabelen for å være
#0. I for løkken går programmet gjennom hver verdi i ordboken og summerere dem sammen og lagres i variabelen tall. En ny variabel gjennomsnitt
#deler summen av alle verdiene i ordboken med antall verdier i ordboken. Gjennomsnitt returneres til der funksjonen blir kalt på, som blir
#lagret i en ny variabel. Deretter printes gjennomsnittet med tekst. 
#4

def gjennomsnittSalg(parameter1):
    tall=0
    for navn,verdi in parameter1.items():
        nummer=int(verdi)
        tall= tall + nummer
        gjennomsnitt=tall/len(parameter1)
    return gjennomsnitt

gjennomsnitt=gjennomsnittSalg(ordbok)
print("Gjennomsnittlig antall salg per salgsperson: ", gjennomsnitt)

#Først defineres en ordbok, deretter defineres en prosedyre hovedprogram. Prosdyren kalles på med en txt fil som argument.
##Inni funksjonen lagres filen i minfil2 variabelen. For løkken går gjennom hver linje i filen og splitter den for
#hver bit på hver linje. De første bitene på hver linje lagres i navn variabelen, og de andre bitene på hver linje
#lagres i verdi. navn og verdi blir lagt inn i ordbok2. Prosedyren maanedensSalgsperson med ordbok2 som argument kalles på
#og kjøres, og selgeren med mest salg blir printet med tekst. Deretter blir antall selgere printet. totalAntallSalg funksjonen
#blir kalt på med ordbok2 som argument. Funksjonen kjøres og returnerer summen av salg lagt sammen, lagres i en ny variabel
#og detter printes den med tekst. Funksjonen gjennomsnittSalg med orbok2 som argument kalles på og blir kjørt. Gjennomsnittet
#blir returnert, lagret i en ny variabel og printes deretter med tekst.
 
#5

ordbok2={}
def hovedprogram(filnavn):
    minfil2=open(filnavn)
    for linje in minfil2:
        biter=linje.split()
        navn=biter[0]
        verdi=int(biter[1])
        ordbok2[navn]= verdi
    maanedensSalgsperson(ordbok2)
    print("Aktive selgere denne maaneden:", len(ordbok2))
    summen=totalAntallSalg(ordbok2)
    print("Totalt antall salg:", summen)
    gjennomsnitt=gjennomsnittSalg(ordbok2)
    print("Gjennomsnittlig antall salg per salgsperson:", gjennomsnitt)
    
    
hovedprogram("salgstall.txt")