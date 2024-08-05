my_list = []

text = input('Iveskite teksta: ')

my_list.append(text.split())
print(my_list)

my_list.insert(0, "Labas!")
my_list.remove('Labas!')


print(len(my_list)) # kiek sarase nariu
print(my_list.count("Labas!"))
