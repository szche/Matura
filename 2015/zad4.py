wiecej_zer_niz_jedynek = []
podzielna_2 = []
podzielna_8 = []

najmniejsza = []
najwieksza = []

with open("DANE/liczby.txt", "r") as file:
    for nr, line in enumerate(file):
        if line.endswith("\n"):
            line = line[:len(line) -1]

        # A)
        if line.count("0") > line.count("1"):
            wiecej_zer_niz_jedynek.append(line)

        # B)
        if line[-1] == "0":
            podzielna_2.append(line)
        if line[-1:-4:-1] == "000":
            podzielna_8.append(line)

        # C)
        if nr == 0:
            najmniejsza = [line, nr+1]
            najwieksza = najmniejsza
        if int(line, 2) > int(najwieksza[0], 2):
            najwieksza = [line, nr+1]
        if int(line, 2) < int(najmniejsza[0], 2):
            najmniejsza = [line, nr+1]

print("-" * 40)
print("WYNIKI")
print("4.1)", len(wiecej_zer_niz_jedynek))
print("4.2)", len(podzielna_2))
print(len(podzielna_8))
print("4.3)", "Najwieksza jest {} w linii {}, a najmniejsza jest {} w linii {}".format(najwieksza[0], najwieksza[1], najmniejsza[0], najmniejsza[1]))
