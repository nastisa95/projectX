# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. 
# Initiate class and show up some calculations.

class Numbers:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

class Calculator(Numbers):
    def __init__(self, a: int, b: int):
        super().__init__(a, b)
        self.add = a + b
        self.subtract = a - b
        self.multiply = a * b
        self.divide = a / b 

    def print_results(self):
        print(f"Sum: {self.add}")
        print(f"Difference: {self.subtract}")
        print(f"Product: {self.multiply}")
        print(f"Quotient: {self.divide}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

calc = Calculator(a, b)

calc.print_results()
