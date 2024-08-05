# Parašykite python programą, kuri susumuoja visus list elementus 
# (visi list elementai yra int arba float tipo. List'a sukurkite patys).

list = [99, 55, 889, 62, 1]
sum = 0
for number in list:
    sum += number

print(f"Visų elementų sąraše suma: {sum}")