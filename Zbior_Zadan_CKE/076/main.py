with open("DANE/szyfr1.txt", "r") as file1:
    teksty1 = [line.strip() for line in file1]
    klucz1 = teksty1[-1].split()
    teksty1.pop(-1)

with open("DANE/szyfr2.txt", "r") as file2:
    teksty2 = [line.strip() for line in file2]
    klucz2 = teksty2[-1].split()
    teksty2.pop(-1)
    teksty2 = "".join(teksty2)

with open("DANE/szyfr3.txt", "r") as file3:
    for line in file3:
        tekst3 = line.strip()

def przedluz_klucz(tekst, k):
    nowy_klucz = []
    if len(tekst) >= len(k):
        nowy_klucz = k
    for x, znak in enumerate(tekst[len(k)::]):
        nowy_klucz.append(nowy_klucz[x])
    return nowy_klucz

def zaszyfruj(tekst, klucz):
    zaszyfrowane = list(tekst)
    placeholder = ""
    for x, numer in enumerate(klucz):
        numer = int(numer) - 1
        placeholder = zaszyfrowane[x]
        zaszyfrowane[x] = zaszyfrowane[numer]
        zaszyfrowane[numer] = placeholder
    return "".join(zaszyfrowane)

def odszyfruj(tekst, klucz):
    odszyfrowane = list(tekst)
    placeholder = ""
    for i in range(len(tekst))[::-1]:
        placeholder = odszyfrowane[i]
        odszyfrowane[i] = odszyfrowane[int(klucz[i])-1]
        odszyfrowane[int(klucz[i])-1] = placeholder
    return "".join(odszyfrowane)

zaszyfrowane1 = []
#Plik 1
for tekst in teksty1:
    klucz_tekst = przedluz_klucz(tekst, klucz1)
    zaszyfrowane1.append(zaszyfruj(tekst, klucz_tekst))

#Plik 2
klucz_plik2 = przedluz_klucz(teksty2, klucz2)
zaszyfrowane2 = zaszyfruj(teksty2, klucz_plik2)

#Plik 3
klucz_plik3 = przedluz_klucz(tekst3, ["6", "2", "4", "1", "5", "3"])
odszyfrowane3 = odszyfruj(tekst3, klucz_plik3)

print("-" * 40)
print("76.1) Teksty zaszyfrowane z pierwszego pliku:")
for tekst in zaszyfrowane1:
    print(tekst)
print("-" * 20)
print("76.2) Tekst zaszyfrowany z drugiego pliku:")
print(zaszyfrowane2)
print("-" * 20)
print("76.3) Tekst odszyfrowany z trzeciego pliku:")
print(odszyfrowane3)
