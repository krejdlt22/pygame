# SOUBORY

# otevreni souboru ('r' znamena pro cteni)
soubor = open('../data/ucitele.txt', 'r', encoding = 'utf-8')

# nacteni celeho souboru naraz (jako jeden string)
# cely_soubor = soubor.read()
# print(cely_soubor)

# nacteni radku souboru
print(soubor.readline()) # prvni radek souboru (vcetne symbolu konce radku!)
print(soubor.readline()) # dalsi radek souboru
print(soubor.read()) # zbytek souboru

# zavreni souboru (co nejdrive)
soubor.close()

# nacteni obsahu souboru do datove struktury
soubor = open('../data/ucitele.txt', 'r', encoding = 'utf-8')

ucitele = []
for dalsi_radek in soubor:
    ucitel = dalsi_radek[:-1] # oriznuti symbolu konce radku
    ucitele.append(ucitel)
else:
    print(ucitele)

soubor.close()

# uprava dat (v pameti)
ucitele.append('Jan Dvořák')

# zapis zmenenych dat do souboru (puvodni obsha se prepise)
soubor = open('../data/ucitele.txt', 'w', encoding = 'utf-8')

for ucitel in ucitele:
    soubor.write(ucitel + '\n')

soubor.close()

