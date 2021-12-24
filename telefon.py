ordbok= {}

def innlesing(filnavn):
    minfil=open(filnavn)
    for linje in minfil:
        biter=linje.split()
        navn=biter[0]
        verdi=int(biter[1])
        ordbok[navn]= verdi
    return ordbok

innlesing("lesfil.txt")
print(innlesing("lesfil.txt"))

