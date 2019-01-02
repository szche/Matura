klucz = 107
#Poczatek Ascii = A = 65
#Koniec Ascii = Z = 90


#6.1
with open("DANE/dane_6_1.txt", "r") as file:
    slowaZaszyfruj = [line.strip() for line in file]

zaszyfrowane_slowa = []


for word in slowaZaszyfruj:
    zaszyfrowany = ""
    for char in word:
        charZaszyfrowany = ord(char) + klucz

        while charZaszyfrowany > 90:
            charZaszyfrowany -= 26
        zaszyfrowany += chr(charZaszyfrowany)
    zaszyfrowane_slowa.append(zaszyfrowany)

with open("wyniki_6_1.txt", "w") as writeFile1:
    writeFile1.write("\n".join(zaszyfrowane_slowa))



#6.2
with open("DANE/dane_6_2.txt", "r") as file2:
    slowaOdszyfruj = [line.strip().split() for line in file2]

odszyfrowane_slowa = []
for word in slowaOdszyfruj:

    #W PLIKU BRAKUJE JEDNEGO KLUCZA
    try:
        klucz = int(word[1])
    except:
        klucz = 0

    odszyfrowany = ""
    for char in word[0]:
        charOdszyfrowany = ord(char) - klucz

        while charOdszyfrowany < 65:
            charOdszyfrowany += 26
        odszyfrowany += chr(charOdszyfrowany)
    odszyfrowane_slowa.append(odszyfrowany)

with open("wyniki_6_2.txt", "w") as writeFile2:
    writeFile2.write("\n".join(odszyfrowane_slowa))


#6.3
bledne = []

with open("DANE/dane_6_3.txt", "r") as file3:
    zaszyfrowane_odszyfrowane = [line.strip().split() for line in file3]

for pair in zaszyfrowane_odszyfrowane:
    odszyfrowane = pair[0]
    zaszyfrowane = pair[1]

    klucz = ord(zaszyfrowane[0]) - ord(odszyfrowane[0])
    if klucz < 0:
        klucz += 26

    #ZASZYFROWANIE PONOWNE TEKSTU I PORÓWNANIE Z PODANYM W PLIKU ZASZYFROWANYM TEKSTEM
    zaszyfrowanyTest = ""
    for char in odszyfrowane:
        charZaszyfrowanyTest = ord(char) + klucz

        while charZaszyfrowanyTest > 90:
            charZaszyfrowanyTest -= 26

        zaszyfrowanyTest += chr(charZaszyfrowanyTest)

    #JESLI WYSTAPIL BLAD W SZYFROWNAIU
    if zaszyfrowanyTest != zaszyfrowane:
        bledne.append(odszyfrowane)

with open("wyniki_6_3.txt", "w") as writeFile3:
    writeFile3.write("\n".join(bledne))
