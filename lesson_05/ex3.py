# Sukurkite string iš daugybės žodžių: Apskaičiuokite, kiek žodžių turi raidę e.

names = input("Įveskite sakinį, sudarytą iš daugybės žodžių: ")
words = names.split()
kiekis = sum(1 for word in words if "e" in word.lower())
print(f"Kiekis žodžių, kurie turi raidę 'e': {kiekis}")
