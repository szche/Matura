
with open("DANE/ciagi.txt", "r") as file:
    wszystko = [line.strip() for line in file]


def czy_dwucykliczny(ciag):
    if len(ciag)%2 != 0:
        return False
    if ciag[0:len(ciag)//2] == ciag[len(ciag)//2:]:
        return True
    else:
        return False

def is_prime(liczba):
    prime = True
    if liczba == 1:
        return False
    for i in range(2, (liczba//2)+1):
        if liczba%i == 0:
            prime = False
            break
    return prime

def czy_popierwsza(liczba, dzielniki):
    for dzielnik1 in dzielniki:
        for dzielnik2 in dzielniki:

            if dzielnik1 * dzielnik2 == liczba:
                return True
    return False

def znajdz_pierwsze_dzielniki(liczba):
    #print(liczba)
    dzielniki = []
    for i in range(1, liczba+1):
        if liczba%i == 0 and is_prime(i) == True:
            dzielniki.append(i)
    #print(liczba, dzielniki)
    return czy_popierwsza(liczba, dzielniki)

dwucykliczne = []
bez2jedynek = []
liczby_polpierwsze = []
for item in wszystko:
    if czy_dwucykliczny(item):
        dwucykliczne.append(item)
    if "11" not in item:
        bez2jedynek.append(item)
    if znajdz_pierwsze_dzielniki(int(item, 2)):
        liczby_polpierwsze.append(int(item, 2))

       
print("-" * 40)
print("Istnieje {} ciagow dwucyklicznych: ".format(len(dwucykliczne)))
print("\n".join(dwucykliczne))
print("-" * 40)

print("{} ciagow nie posiada sasiadujacych jedynek".format(len(bez2jedynek)))
print("-" * 40)

print("{} ciagow sa polpierwsze, najwieksza z nich to {}, a najmniejsza to {}".format(len(liczby_polpierwsze), max(liczby_polpierwsze), min(liczby_polpierwsze)))
print("-" * 40)

