wiecej_zer_jedynek = []
podzielne_2 = []
podzielne_8 = []
najwieksza = []
najmniejsza = []
with open("DANE/liczby.txt", "r") as file:
    for x, line in enumerate(file):
        line = line.strip()
        if line.count("0") > line.count("1"):
            wiecej_zer_jedynek.append(line)
        if int(line, 2)%2 == 0:
            podzielne_2.append(line)
        if int(line, 2)%8 == 0:
            podzielne_8.append(line)

        if x == 0:
            najwieksza = [line, x]
            najmniejsza = [line, x]
        elif int(najwieksza[0], 2) < int(line, 2):
            najwieksza = [line, x]
        elif int(line,2) < int(najmniejsza[0], 2):
            najmniejsza = [line,x]

print("-" * 40)
print("1) Jest {} takich liczb".format(len(wiecej_zer_jedynek)))
print("2) Podzielne przez 2: {}\nPodzielne przez 8: {}".format(len(podzielne_2), len(podzielne_8)))
print("3) Najwieksza liczba to {} w wierszu {}\nNajmniejsza liczba to {} w wierszu {}".format(najwieksza[0], najwieksza[1]+1, najmniejsza[0], najmniejsza[1]+1))

