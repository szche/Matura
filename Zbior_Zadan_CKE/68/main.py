with open("DANE/dane_napisy.txt", "r") as file:
    zbiory = [line.strip().split() for line in file]


def slownik_czestosci(napis):
    slownik = {}
    for char in napis:
        if char.upper() not in slownik:
            slownik[char.upper()] = 1
        else:
            slownik[char.upper()] += 1
    return slownik

#bezmyslne znajdowanie k, przydalaby sie poprawka optymalizacyjna
def znajdz_k(tekst):
    k = 0
    slownik_podstawowy = slownik_czestosci(tekst)
    for para in zbiory:
        for napis in para:
            if slownik_czestosci(napis) == slownik_podstawowy:
                k += 1
    return k
            
jednolite = []
anagramy = []
zbior_k = []
for para in zbiory:
    if slownik_czestosci(para[0]) == slownik_czestosci(para[1]):
        anagramy.append(para)
        if len(slownik_czestosci(para[0])) == 1:
            jednolite.append(para)   

    for napis in para:
        zbior_k.append(znajdz_k(napis))
        
print("-" * 40)
print("Jest {} anagramow jednolitych: ".format(len(jednolite)))
for line in jednolite:
    print("\n".join(line))

print("-" * 40)
print("Jest {} anagramow".format(len(anagramy)))


print("-" * 40)
print("Najwieksza liczba k to {}".format(max(zbior_k)))

print("-" * 40)
