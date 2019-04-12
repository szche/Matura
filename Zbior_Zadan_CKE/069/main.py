
with open("DANE/dane_geny.txt", "r") as file:
    baza = [line.strip() for line in file]


def znajdz_genotyp(genotyp):
    genyG = []
    gen = ""
    litera = genotyp[0]
    for x, znak in enumerate(genotyp[1::]):
        if litera + znak == "AA" and len(gen) == 0:
            gen += litera + znak
        elif len(gen) != 0:
            gen += znak
        if litera + znak == "BB" and len(gen) != 0:
            genyG.append(gen)
            gen = ""
        litera = znak
    return genyG

gatunki = {}
z_mutacja = []
najwiecej_genow = 0
najlduzszy_gen = ""
genyOdporne = []
genySuperOdporne = []
for genotyp in baza:
    if len(genotyp) not in gatunki:
        gatunki[len(genotyp)] = 1
    else:
        gatunki[len(genotyp)] += 1
    geny = znajdz_genotyp(genotyp)
    genLewy = znajdz_genotyp(genotyp[::-1])
    if len(geny) > 0:
        if len(geny) > najwiecej_genow:
            najwiecej_genow = len(geny)
        for gen in geny:
            mutacjaDodana = False
            if "BCDDC" in gen and mutacjaDodana == False:
                z_mutacja.append(gen)
                mutacjaDodana = True
            if len(gen) > len(najlduzszy_gen):
                najlduzszy_gen = gen
    if geny == genLewy:
        genyOdporne.append(geny)
    if genotyp == genotyp[::-1]:
        genySuperOdporne.append(genotyp)
            
                

print("-" * 40)
print("69.1) Jest {} wszyskich gatunkow, {} reprezentuje jeden gatunek".format(len(gatunki), sorted(gatunki.values())[-1]))
print("69.2) Jest {} osobnikow z mutacja".format(len(z_mutacja)))
print("69.3) Najwiecej jest {} genow, a najdluzszy ma {} znakow".format(najwiecej_genow, len(najlduzszy_gen)))
print("69.4) Genotypow odpornych jest {}, a silnie odpornych {}".format(len(genyOdporne), len(genySuperOdporne)))
