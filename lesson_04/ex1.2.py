#Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

def my_dict(keys: list[int]) -> dict:
    values = [key * key for key in keys]
    return dict((zip(keys, values)))

print(my_dict([1, 6, 9]))
