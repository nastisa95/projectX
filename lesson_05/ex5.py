# Given the same string calculate the occurrence of each letter in the string. 
# (HINT: store everything in dictionary),

names = input("Įveskite sakinį, sudarytą iš daugybės žodžių: ")
how_often = {}

for letter in names:
    if letter in how_often:
        how_often[letter] += 1
    else:
        how_often[letter] = 1 

print("Raidžių dažnumas sakinyje yra: ")
for letter, often in how_often.items():
    print(f"{letter}: {often}")


# Given the same string calculate the occurrence of each letter in the string. (HINT: store everything in dictionary)
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# my_list = list(text)
# print(f"my_list:\n{my_list}")
# occurences = {letter: my_list.count(letter) for letter in my_list if letter != " " and letter != "-" and letter != "."}
# print(occurences)