super_pierwsza_2_1000 = 0
super_pierwsza_100_10000 = 0
super_pierwsza_1000_100000 = 0

suma_pierwsza_100_10000 = 0
suma_super_pierwszych_100_10000 = 0

def is_prime(number):
    prime = True
    for i in range(2, number):
        if number%i == 0:
            prime = False
            break
    return prime

def suma_cyfr(number):
    suma = 0
    for char in str(number):
        suma += int(char)
    return suma


#Pierwszy przedzial
for item in range(2, 1001):
    if is_prime(item) and is_prime(suma_cyfr(item)) and is_prime(suma_cyfr(bin(item)[2:])):
        super_pierwsza_2_1000 += 1

#Drugi przedzial
for item in range(100, 10001):
    if is_prime(item) and is_prime(suma_cyfr(item)) and is_prime(suma_cyfr(bin(item)[2:])):
        super_pierwsza_100_10000 += 1
        suma_super_pierwszych_100_10000 += 1
    if is_prime(suma_cyfr(item)):
        suma_pierwsza_100_10000 += 1


#Trzeci przedzial
for item in range(1000, 100001):
    if is_prime(item) and is_prime(suma_cyfr(item)) and is_prime(suma_cyfr(bin(item)[2:])):
        super_pierwsza_1000_100000 +=1




print(super_pierwsza_2_1000)
print(super_pierwsza_100_10000)
print(super_pierwsza_1000_100000)


print("b)")

print(suma_pierwsza_100_10000)

if is_prime(suma_super_pierwszych_100_10000):
    print("TAK")
else: print("NIE")
