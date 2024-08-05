class Person:  #klase rasoma is didziosios
    def __init__ (self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def travel(self):
        print(f"{self.name} is walking")

    def say_hello(self) -> None:
        print (f"{self.name} shouts Hello!")

class Driver(Person):
    def __init__(self, name: str, car: str, age: int = 0):
        super().__init__(name, age)
        self.car = car

    def travel(self):
        print(f"{self.name} is driving {self.car}")

person_01 = Person("Ana", 30)
person_02 = Driver("Vita", "Totoya", 40)

person_01.say_hello()
person_01.travel()
person_02.say_hello()
person_02.travel()
