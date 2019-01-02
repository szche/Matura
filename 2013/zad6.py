pierwsza_rowna_ostatniej = []
pierwsza_rowna_ostatniej_10 = []
spelnia_warunek_c = []

with open("DANE/dane.txt") as file:
    for line in file:
        line = line.rstrip('\n')

        # A)
        if line[0] == line[-1]:
            pierwsza_rowna_ostatniej.append(line)

        # B)
        if str(int(line, 8))[0] == str(int(line, 8))[-1]:
            pierwsza_rowna_ostatniej_10.append(line)

        spelnia = True
        pierwszy = int(line[0])
        for char in line[1:]:
            if int(char) >= pierwszy:
                pierwszy = int(char)
            else:
                spelnia = False
                break
        if spelnia:
            spelnia_warunek_c.append(int(line))


print(len(pierwsza_rowna_ostatniej))
print(len(pierwsza_rowna_ostatniej_10))
spelnia_warunek_c.sort(reverse = True)
print(len(spelnia_warunek_c), spelnia_warunek_c[0], spelnia_warunek_c[-1])
