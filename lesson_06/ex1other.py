class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

    def subtract(self) -> float:
        return self.a - self.b

    def multiply(self) -> int:
        return self.a * self.b

    def divide(self) -> float:
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

calc = Calculator(a, b)

print(f"{calc.a} + {calc.b} = {calc.add()}")
print(f"{calc.a} - {calc.b} = {calc.subtract()}")
print(f"{calc.a} * {calc.b} = {calc.multiply()}")
print(f"{calc.a} / {calc.b} = {calc.divide()}")
