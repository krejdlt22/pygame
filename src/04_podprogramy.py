# PODPROGRAMY

# definice podprogramu
def pozdrav():
    print('Ahoj!')

# spusteni podprogramu
pozdrav()

# podprogram s parametry (vstupnimi daty)
def pozdrav(koho):
    print('Ahoj, ' + koho + '!')

pozdrav('Hynku')
pozdrav('Viléme') # diky ruznym hodnotam parametru menime konkretni chovani podprogramu
pozdrav('Jarmilo')

# vyse uvedene podprogramy byly tzv. "procedury" -> nevraceji se z nich zadna data
# podprogramy, ktere vraceji (vystupni) data, se nazyvaji "funkce"

def mocnina(ceho, na_co):
    vysledek = ceho ** na_co
    return vysledek

vysledek = mocnina(3, 5) # funkce vraci vysledek, ktery je potreba si ulozit
print(vysledek)

# nyni muzeme pouzivat rekurzi
def faktorial(n):
    if n < 0:
        raise Exception('Faktoriál pro záporná čísla není definován.') # vyjimka
    elif n == 0:
        return 1 # mezni pripad
    else:
        return n * faktorial(n - 1) # rekurzivni volani

print(faktorial(5)) # 120
print(faktorial(0)) # 1
# print(faktorial(-1)) # chyba, skonci vyvolanim vyjimky

