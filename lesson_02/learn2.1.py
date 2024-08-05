my_dictionary = {"name": "Tom", "surname": "Edison"}
print(f"vardas: {my_dictionary['name']}")
print(f"pavarde: {my_dictionary['surname']}")

my_dictionary["car"] = "Tesla"
del my_dictionary['name']
print(my_dictionary)