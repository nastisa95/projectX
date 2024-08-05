# Pabandykite sukurti dict struktūrą, kurioje turite panaudoti visas jums žinomas duomenų struktūras ir tipus.

my_dict = {
    "first_name": "Bender", #tuple->
    "second_names": ("Bending", "Coilette", "Titanius", 'Anglesmith', 'Ramblin', 'Young', 'Biddy', 'Boiler', 'Drunken', 'Garbage', 'Can', 'Boogerbot', 'Blotto', 'Super King'),
    "last_name": "Rodriguez",
    "hates": ["people", "human", "men", "mankind", "mortals"], #list
    "birth_year": 2996, #int
    "loves": {
        "lovely_num": 3.14, #float
        "lovely_human": "Fry",
        "lovely_drink": "beer",
    },#dict
    "unique_hobbies": {"bending", "drinking", "gambling", "smoking"} #set
}

my_dict['hates'].append('water')
print(my_dict)

# print(my_dict["loves"]["lovely_drink"])
