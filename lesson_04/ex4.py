# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes.
words = ["apple", "banana", "cherry", "date", "fig"]
def word_list(words: str) -> list:
    new_set = set(for word in words)
    return unique = [if new_set word for word in words if new_set]
print(unique)
