# VETVENI (ROZHODOVANI)

cislo = int(input('Zadej celé číslo: '))

if cislo > 0:
    print('Číslo', cislo, 'je kladné.')
elif cislo < 0:
    print('Číslo', cislo, 'je záporné.')
else:
    print('Číslo', cislo, 'je nulové.')

# PODMINENY CYKLUS

while cislo > 0:
    print(cislo, end = ' ') # uprava zakonceni vypisu
    #cislo = cislo - 1
    cislo -= 1 # zkraceny zapis
else:
    # toto se stane jen jednou, az opakujici se cast cyklu skonci
    print()

print('Toto se vypíše, až cyklus skončí.')

