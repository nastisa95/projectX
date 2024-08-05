# Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį. 
# Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį. 
# Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.

name = "lacrimosa"
password = "666"  

while True:
    in_1 = input("Įveskite vartotojo vardą: ")
    in_2 = input("Įveskite slaptažodį: ")
    
    if in_1 == name and in_2 == password:
        print("Duomenys teisingi!")
        break
    else:
        print("Neteisingas vartotojo vardas arba slaptažodis. Bandykite dar kartą.")

