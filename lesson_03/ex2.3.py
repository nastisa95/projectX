# Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. 
# Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100.

import random
my_dict = {key: random.randint(1, 100) for key in range(1, 11)}
print(my_dict)
