class SimpleCalculator:

    def addition(self, first_input, second_input):
        return first_input + second_input

    def subtraction(self, first_input, second_input):
        return first_input - second_input

    def multiplication(self, first_input, second_input):
        return first_input * second_input

    def division(self, first_input, second_input):
        return first_input / second_input


calculator = SimpleCalculator()
result = calculator.addition(10, 10)
print(f"Addition : {result}")

result = calculator.subtraction(250.5, 10)
print(f"Subtraction : {result}")

result = calculator.multiplication(10, 10)
print(f"Multiplication : {result}")

result = calculator.division(500, 10)
print(f"Division : {result}")
