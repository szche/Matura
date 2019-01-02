
liczby_parzyste = []
najwieksza  = 0;
suma_9 = 0

with open("DANE/liczby.txt", "r") as file:
    for line in file:
        if line.endswith("\n"):
            line = line[:len(line) - 1]

        # A)
        if line[-1] == "0":
            liczby_parzyste.append(line)

        # B)
        #zamiana z dwojkowego na dziesietny
        line_10 = int(line, 2)

        if line_10 > najwieksza:
            najwieksza = line_10

        # C)
        if len(line) == 9:
            suma_9 += line_10

print("-" * 40)
print("WYNIKI")
print("a)", len(liczby_parzyste))
print("b)", najwieksza, bin(najwieksza)[2:])
print("c)", bin(suma_9)[2:])
