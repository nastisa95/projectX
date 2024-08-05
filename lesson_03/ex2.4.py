# Sukurkite PIN kodo nulaužimo programą. Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys. 
# Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas, 
# kol rasite tą, kurią įvedėte.

i = 1000
pin = int(input("Iveskite 4 skaitmenu skaptazodi: "))

while True:
    i = i + 1
    if i != pin:
        print(f"Pin {i} neteisingas")
    else:
        print (f"Pin {i} teisingas")
        break