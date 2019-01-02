with open("DANE/sygnaly.txt" ,"r") as file:
    sygnaly = [line.strip() for line in file]


#4.1
przeslanie = ""
for slowo in sygnaly[39::40]:
    przeslanie += slowo[9]




def czestosc(slowo):
    slownik_czestosci = {}
    for char in slowo:
        slownik_czestosci[char] = slowo.count(char)
    return len(slownik_czestosci)

def wartosc_bezwgledna(liczba):
    if liczba < 0:
        return -liczba
    else:
        return liczba


def odlegosci(word):
    prawidlowo = True
    previous_char = word[0]
    for char in word[1::]:
        if wartosc_bezwgledna(ord(char) - ord(previous_char)) <= 10:
            prawidlowo = True
        else:
            prawidlowo = False
            break
        previous_char = char

    return prawidlowo


slowo_najwiecej = ""
nie_przekraczajace_odleglosci = []
for slowo in sygnaly:

    #4.2
    if czestosc(slowo) > czestosc(slowo_najwiecej):
        slowo_najwiecej = slowo

    #4.3
    if odlegosci(slowo):
        nie_przekraczajace_odleglosci.append(slowo)


print("-" * 40)
print("WYNIKI")
with open("wyniki4.txt", "w") as wyniki:
    wyniki.write("4.1 Przeslanie to {} \n".format(przeslanie))
    wyniki.write("4.2 Najwieksza licze roznych liter ma {} z iloscia {}\n".format(slowo_najwiecej, czestosc(slowo_najwiecej)))
    wyniki.write("4.3 Slowa nie przekraczajce odlegosci to {}\n".format("\n".join(nie_przekraczajace_odleglosci)))
