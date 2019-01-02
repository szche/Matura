alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted_words = []
decrypted_words = []

with open("DANE/tj.txt", "r") as niezaszyfrowane, open("DANE/klucze1.txt", "r") as klucze:
    for line in niezaszyfrowane:
        slowo = line.strip()
        klucz = klucze.readline().strip()
        zaszyfrowany = ""

        while len(slowo) > len(klucz):
            klucz += klucz


        for nr, char in enumerate(slowo):
            char_encrypted = ord(slowo[nr]) + (alfabet.find(klucz[nr])+1)
            while char_encrypted > 90:
                char_encrypted -= 26

            zaszyfrowany += chr(char_encrypted)

        encrypted_words.append(zaszyfrowany)




with open("wynik4a.txt", "w") as zadA:
    zadA.write("\n".join(encrypted_words))




with open("DANE/sz.txt", "r") as zaszyfrowane, open("DANE/klucze2.txt", "r") as klucze:
    for line in zaszyfrowane:
        slowo = line.strip()
        klucz = klucze.readline().strip()
        zaszyfrowany = ""

        while len(slowo) > len(klucz):
            klucz += klucz

        for nr, char in enumerate(slowo):
            char_encrypted = ord(slowo[nr]) - (alfabet.find(klucz[nr])+1)

            while char_encrypted < 65:
                char_encrypted += 26

            zaszyfrowany += chr(char_encrypted)

        decrypted_words.append(zaszyfrowany)



with open("wynik4b.txt", "w") as zadA:
    zadA.write("\n".join(decrypted_words))
