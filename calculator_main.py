class Calculator:
    def __init__(self):
        self.memory = 0 # Current calculator number is zero as non of the actions was done yet.

    # Method which will add number to the current memory
    def addition(self, number):
        self.memory += number

    # Method which will subtract number from current memory
    def subtraction(self, number):
        self.memory -= number

    # Method which will perform multiplication on current memory by number defined
    def multiplication(self, number):
        self.memory *= number

    # Method which will divide current memory by number defined
    def division(self, number):
        self.memory /= number

    # Method which will take (n) root of a number where n = number
    def root(self, number):
        self.memory **= 1/number

    # Method which will check current calculator memory
    def get_memory(self):
        return self.memory

    # Method which will reset current memory to initial value (zero)
    def reset_memory(self):
        self.memory = 0
