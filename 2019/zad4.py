from math import gcd

with open("Dane_PR2/liczby.txt", "r") as f:
    liczby = [int(line.strip()) for line in f] 

# 4.1
def sprawdz_potege(liczba):
    for i in range(0, liczba):
        if 3**i == liczba: return True
        elif 3**i > liczba: return False

# 4.2
def silnia(liczba):
    wynik = 1
    for i in range(1, liczba + 1):
        wynik *= i
    return wynik

# 4.2
def suma_silni(liczba):
    suma = 0
    for cyfra in str(liczba):
        suma += silnia( int(cyfra) )
    if suma == liczba: return True
    return False
        


potegi3 = 0
rowne_silni = []

for liczba in liczby:
    if sprawdz_potege(liczba) == True:
        potegi3 += 1
    if suma_silni(liczba) == True:
        rowne_silni.append(liczba)

# 4.3
odp = [0, 0, 0] #Pierwsza liczba - Dlugosc Ciagu - Najwiekszy wspolny dzielnik
for counter, poczatek in enumerate(liczby):
    ostatni_gcd = poczatek 
    ciag = 1 
    for n in liczby[counter+1:]:
        if gcd(ostatni_gcd, n) > 1:
            ostatni_gcd = gcd(ostatni_gcd, n)
            ciag += 1
        else:
            if ciag > odp[1]:
                odp = [poczatek, ciag, ostatni_gcd]
            break


print("4.1:", potegi3)
print("4.2:", rowne_silni)
print("4.3:", odp)
    
