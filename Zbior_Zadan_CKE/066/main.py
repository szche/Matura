import math

with open("DANE/trojki.txt", "r") as file:
    zestawy = [line.strip().split() for line in file]

def sortuj(e):
    return int(e)


def suma_cyfr(liczba):
    suma = 0
    for number in liczba:
        suma += int(number)
    return suma

def is_prime(liczba):
    if int(liczba) == 1: return False
    prime = True
    for i in range(2, (int(liczba)//2)+1):
        if int(liczba) % i == 0:
            prime = False
            break
    return prime


def jest_trojkatem_prostokatnym(para_liczb):
    para_liczb.sort(key=sortuj)
    if (math.pow(int(para_liczb[0]), 2) + math.pow(int(para_liczb[1]), 2)) == math.pow(int(para_liczb[2]), 2):
        return True
    return False

def jest_trojkatem(para_liczb):
    if (int(para_liczb[0]) + int(para_liczb[1])) > int(para_liczb[2]):
        return True
    return False
    
warunek1 = []
warunek2 = []
warunek3 = []
warunek4 = []
dl_warunek4 = 0
for row in zestawy:
    if suma_cyfr(row[0]) + suma_cyfr(row[1]) == int(row[2]):
        warunek1.append(" ".join(row))
    if is_prime(row[0]) and is_prime(row[1]) and int(row[0]) * int(row[1]) == int(row[2]):
        warunek2.append(" ".join(row))

    if jest_trojkatem_prostokatnym(row):
        warunek3.append(" ".join(row))
    else:
        warunek3.append("-")
        
    if jest_trojkatem(row):
        warunek4.append(" ".join(row))
        dl_warunek4 += 1
    else:
        warunek4.append("-")

print("-" * 40)
print("Zestawy liczb spelniajace pierwszy warunek: ")
print("\n".join(warunek1))
print("-" * 40)


print("Zestawy liczb spelniajace drugi warunek: ")
print("\n".join(warunek2))
print("-" * 40)

print("Zestawy liczb spelniajace trzeci warunek: ")
for counter, item in enumerate(warunek3[1::]):
    if item != "-" and warunek3[counter+1] != "-":
        print(item)
print("-" * 40)

print("Jest {} bedacych mozliwymi trojkatami".format(dl_warunek4))
najdluzszy_ciag = []
dlugosc = 0
for item in warunek4:
    if item != "-":
        dlugosc += 1
    else:
        najdluzszy_ciag.append(dlugosc)
        dlugosc = 0
print("Najdluzszy ciag ma {} elementow".format(max(najdluzszy_ciag)))
print("-" * 40)

