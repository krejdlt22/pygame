# textovy vystup
print('Hello world!')

# textovy vstup
zadani = input('Zadej něco: ')
# zadani je PROMENNA, do ktere jsem si pomoci = ulozil hodnotu
# = je tzv. operator PRIRAZENI

# promenna zadani nyni obsahuje to, co uzivatel zadal
print('Zadal jsi:', zadani)
print('Zadal jsi: ' + zadani)

# operator + lepi text k sobe (tzv. zretezeni)
print('abcd' + 'efgh')

# DATOVE TYPY

# (1) string (text)
print('abcd') # muzeme pouzivat ' uvozovky
print("abcd") # muzeme pouzivat " uvozovky
print('abcd' + "efgh")

print('ab' * 10) # string lze nasobit cislem

# (2) integer (cele cislo)
print(50)

print(1 + 1) # soucet
print(1 - 1) # rozdil
print(100 * 12) # soucin
print(100 / 12) # podil
print(10 // 4) # celociselne deleni
print(10 % 4) # zbytek po celociselnem deleni
print(3 ** 4) # mocnina

print(100 + int('100')) # int() prevadi data na integery
print(str(100) + '100') # str() prevadi data na stringy

# (3) floating point (necele cislo)
print(3.14)
# POZOR, necela cast zacina . ne ,
print(3,14) # toto jsou dve cisla 3 a 14

# odmocnina pomoci neceleho cisla
print(2 ** 0.5)
# odmocnina pomoci zlomku
print(2 ** (1/2))

print(str(3.14) + ' je přibližná hodnota Pi.')

print(float('1.2345') - 1) # float() prevadi data na floaty
# POZOR na zaokrouhlovaci chyby

# (4) boolean (pravdivost)
print(True)
print(False)

# logicke operace
print(True and True)
print(True or False)
print(not False)

# porovnavaci operace produkuji booly!
print(5 > 2)
print(5 < 2)
print(5 >= 2)
print(5 <= 2)

print(5 == 2) # ROVNO
print(5 != 2) # NEROVNO

# Q & A
print(0.99999) # floatove "skoro 1"
print(int(0.99999)) # integerove "nula" (zaokrouhleno dolu)

print(10) # integerove 10
print(float(10)) # floatove 10.0

# prvni mala aplikace
a = float(input('Zadej číslo: '))
b = float(input('Zadej číslo: '))

print('Součin tvých čísel je', a * b)

