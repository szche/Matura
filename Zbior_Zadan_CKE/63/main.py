with open("DANE/ciagi.txt", "r") as file:
    wszystko = [line.strip() for line in file]


def czy_dwucykliczny(ciag):
    if len(ciag)%2 != 0:
        return False
    if ciag[0:len(ciag)//2] == ciag[len(ciag)//2:]:
        return True
    else:
        return False


dwucykliczne = []
bez2jedynek = []
for item in wszystko:
    if czy_dwucykliczny(item):
        dwucykliczne.append(item)
    if "11" not in item:
        bez2jedynek.append(item)
    czy_polpierwsza(int(item, 2))
       
print("-" * 40)
print("Istnieje {} ciagow dwucyklicznych: ".format(len(dwucykliczne)))
print("\n".join(dwucykliczne))
print("-" * 40)

print("{} ciagow nie posiada sasiadujacych jedynek".format(len(bez2jedynek)))
print("-" * 40)
