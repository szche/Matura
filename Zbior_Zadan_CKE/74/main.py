with open("DANE/hasla.txt", "r") as file:
    hasla = [line.strip() for line in file]



cyfry = "0123456789"
alfabet_lower = "abcdefghijklmnopqrstuvwxyz"
alfabet_upper = alfabet_lower.upper()

def ciag_ASCII(haslo):
    global cyfry, alfabet_lower, alfabet_upper
    #Podziel haslo na odcinki o dlugosci 4 znakow
    for i in range(-1, len(haslo)-4):
        odcinek = haslo[i+1::][:4]
        zawiera = True
        if odcinek[0] in cyfry:
            rodzaj = cyfry
        elif odcinek[0] in alfabet_lower:
            rodzaj = alfabet_lower
        elif odcinek[0] in alfabet_upper:
            rodzaj = alfabet_upper
        for znak in odcinek[1::]:
            if znak not in rodzaj:
                zawiera = False
                break
        if zawiera:
            return True
    return False


def czy_zawiera(haslo):
    global cyfry, alfabet_lower, alfabet_upper
    maCyfre = False
    maLitereM = False
    maLitereD = False
    for znak in haslo:
        if znak in cyfry:
            maCyfre = True
        elif znak in alfabet_lower:
            maLitereM = True
        elif znak in alfabet_upper:
            maLitereD = True
    if maCyfre and maLitereM and maLitereD:
        return True
    return False
            

podpunkt_1 = []
podpunkt_2 = []
podpunkt_3 = []
podpunkt_4 = []
for haslo in hasla:
    sameCyfry = True
    for znak in haslo:
        if znak not in cyfry:
            sameCyfry = False
            break
    if sameCyfry:
        podpunkt_1.append(haslo)
    if hasla.count(haslo) > 1:
        if haslo not in podpunkt_2:
            podpunkt_2.append(haslo)
    if ciag_ASCII(haslo) == True:
        podpunkt_3.append(haslo)
    if czy_zawiera(haslo) == True:
        podpunkt_4.append(haslo)




print("-" * 40)
print("74.1) Jest {} takich hasel".format(len(podpunkt_1))) 
print("74.2) Hasla uzyte wiecej niz dwa razy: ")
for haslo in sorted(podpunkt_2):
    print(haslo)
#Wedlug odpowiedzi ten wynik jest bledny, ale jak wyprintujesz sobie te hasla to wszystko sie zgadza (?)
print("74.3) Jest {} hasel z ciagiem ASCII".format(len(podpunkt_3)))
print("74.4) Jest {} hasel spelniajacych ten warunek".format(len(podpunkt_4)))


