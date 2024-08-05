class Person:  #klase rasoma is didziosios
    def __init__ (self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self) -> None:
        print (f"{self.name} shouts Hello!")

person_01 = Person("Ana", 30)
person_02 = Person("Vita", 40)
print(person_01.name)
print(person_02.say_hello())
