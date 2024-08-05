# Naudodami tą patį string, kaip ir ankstesniame pratime: apskaičiuokite raidžių, 
# kurios turi daugiau nei 5 simbolius, skaičių.

names = input("Įveskite sakinį, sudarytą iš daugybės žodžių: ")
words = names.split()
kiekis = sum(1 for word in words if len(word)>5)
print(f"Kiekis žodžių, kurie turi daugiau nei 5 simbolius: {kiekis}")
