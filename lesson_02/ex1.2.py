# Parašykite python programą, kuri padaugina visus list elementus 
# (visi list elementai yra int arba float tipo. List'a sukurkite patys).

list = [99, 55, 889, 62, 1]
a = 1
for number in list:
    a *= number

print(f"Visų elementų sąraše sandauga  lygi: {a}")