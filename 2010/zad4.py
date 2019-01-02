ta_sama_liczba_znakow = []
zbior_anagramow = []

def slownik_czestosci(item):
    slownik = {}

    for char in item:
        if char not in slownik:
            slownik[char] = 1
        else:
            slownik[char] += 1
    return slownik


with open("DANE/anagram.txt", "r") as file:
    for line in file:
        tablica_slow = []
        if line.endswith("\n"):
            line = line[:len(line) - 1]

        tablica_slow = line.split()

        # A)
        liczba_slow_pierwsze = len(tablica_slow[0])
        jednakowa_liczba = True
        for item in tablica_slow[1:]:
            if len(item) != liczba_slow_pierwsze:
                jednakowa_liczba = False
                break
        if jednakowa_liczba:
            ta_sama_liczba_znakow.append(" ".join(tablica_slow))

        # B)
        #tworzymy tzw. słownik częstości, który potem porównujemy z każdym kolejnym wyrazem
        pierwsze_slowo = tablica_slow[0]
        slownik_pierwszy = slownik_czestosci(pierwsze_slowo)
        anagramy = True
        for word in tablica_slow[1:]:
            if slownik_czestosci(word) != slownik_pierwszy:
                anagramy = False
                break

        if anagramy:
            zbior_anagramow.append(" ".join(tablica_slow))


print("-" * 40)
print("WYNIKI")

with open("odp_4a.txt", "w") as odpA:
    for line in ta_sama_liczba_znakow:
        odpA.write(line + "\n")

with open("odp_4b.txt", "w") as odpB:
    for line in zbior_anagramow:
        odpB.write(line + "\n")
