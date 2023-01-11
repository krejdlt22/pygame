# DATOVE STRUKTURY

# 1) tuple (n-tice)

budovy = ('S101', 'H59', 'H618', 'OPMB')
# indexy     0      1       2       3

print(budovy[1]) # H59

# budovy[1] = 'H11' # chyba, tuple nelze menit
budovy = ('H11', 'H1') # povoleno, prepisuje se cela promenna
print(budovy[1]) # H1


# 2) list (seznam)

ucitele = ['Šenkýř', 'Bárta', 'Marcinčín']
# indexy       0        1            2

print(ucitele[1])

ucitele[1] = 'Klázar' # polozky lze menit
print(ucitele[1])

ucitele.append('Kábrle') # polozky lze pridavat
print(ucitele)

ucitele.remove('Marcinčín') # polozky lze odebirat
print(ucitele)

ucitele.append('Lukáčková')
ucitele.append('Jindová')
ucitele.append('Šandová')
ucitele.append('Matějec')

# seznamy lze SLICOVAT

print(ucitele[2])   # polozka s indexem 2
print(ucitele[2:])  # polozky od indexu 2 dale
print(ucitele[:2])  # polozky od zacatku do indexu 2 (bez)
print(ucitele[2:5]) # polozky od indexu 2 (vcetne) do indexu 5 (bez)
print(ucitele[:])   # kopie struktury

print(ucitele[-1]) # prvni polozka od konce
print(ucitele[-3:]) # tri posledni polozky

print(len(ucitele)) # pocet ucitelu


# 3) dictionary (slovnik)

zamestnanec = {'krestni': 'Jan', 'prijmeni': 'Novák'}

print(zamestnanec)
print(zamestnanec['prijmeni'])

zamestnanec['plat'] = 123456
print(zamestnanec)


# CYKLUS for PRO PRACI S DAT. STRUKTURAMI

for ucitel in ucitele:
    print(ucitel)

for budova in budovy:
    print(budova)

for klic in zamestnanec:
    print(klic, zamestnanec[klic])

for i in range(10): # cisla od 0 do 9
    print(i, end = ' ')
else:
    print()

for i in range(1, 10): # cisla od 1 do 10 (bez)
    print(i, end = ' ')
else:
    print()

for i in range(10): # cisla od 0 do 9
    print(i + 1, end = ' ') # vypisuji se cisla od 1 do 10
else:
    print()

for index, ucitel in enumerate(ucitele):
    print(str(index) + ': ' + ucitel)

x = 1, 2, 3 # take tuple
print(x) # (1, 2, 3)
a, b, c = x # vytazeni jednotlivych hodnot z tuplu
print(b) # 2

print(ucitele.index('Šenkýř')) # pozice hodnoty v seznamu

print(list(zamestnanec.keys())) # seznam klicu slovniku

