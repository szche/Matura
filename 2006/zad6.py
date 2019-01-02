
dziennik_czestosci = {}
wystepuje_wiecej_niz_raz = []

liczby_parzyste_szesnastkowe = ["A", "C", "E"]

liczby_parzyste = []
palindromy = []

def palindrom(tekst):

    indeks = -1
    te_same = 0
    for char in tekst[:len(tekst)//2]:
        if char == tekst[indeks]:
            te_same += 1
        indeks -= 1
    if te_same >= len(tekst)//2:
        return True
    return False


with open("DANE/dane.txt", "r") as file:
    for line in file:
        if line.endswith("\n"):
            line = line[:len(line) - 1]

        #A)
        if line not in dziennik_czestosci:
            dziennik_czestosci[line] = 1
        else:
            dziennik_czestosci[line] += 1

        # B)
        if line[-1] in liczby_parzyste_szesnastkowe:
            liczby_parzyste.append(line)
        #C)
        if palindrom(line):
            palindromy.append(line)

# A)
najczesciej = 0
item_najczesciej = ""
for item in dziennik_czestosci:
    if dziennik_czestosci[item] > 1:
        wystepuje_wiecej_niz_raz.append(item)

    if dziennik_czestosci[item] > najczesciej:
        najczesciej = dziennik_czestosci[item]
        item_najczesciej = item


print("-" * 40)
print("WYNIKI")
print("a)",len(wystepuje_wiecej_niz_raz))
print("Najczesciej wystepuje {}, bo {} razy".format(item_najczesciej, najczesciej))
print("b)", len(liczby_parzyste))
print("c)", len(palindromy))