#Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.

def adding(words: list[str]) -> list[str]:
    end = "ing"
    return [word + end for word in words]

print(adding(["play", "sing", "sleep"]))
