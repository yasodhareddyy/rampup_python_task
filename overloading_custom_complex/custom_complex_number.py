class CustomComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        # Addition
        real = self.real + other.real
        imag = self.imag + other.imag
        return CustomComplex(real, imag)

    def subtract(self, other):
        # Subtraction
        real = self.real - other.real
        imag = self.imag - other.imag
        return CustomComplex(real, imag)

    def multiply(self, other):
        # Multiplication
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return CustomComplex(real, imag)

    def equal(self, other):
        # Equality comparison
        return self.real == other.real and self.imag == other.imag

    def not_equal(self, other):
        # Inequality comparison
        return not self.equal(other)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

# Example usage:
c1 = CustomComplex(3, 4)
c2 = CustomComplex(1, 6)

# Addition
result_add = c1.add(c2)
print(f"Addition: {c1} + {c2} = {result_add}")

# Subtraction
result_sub = c1.subtract(c2)
print(f"Subtraction: {c1} - {c2} = {result_sub}")

# Multiplication
result_mul = c1.multiply(c2)
print(f"Multiplication: {c1} * {c2} = {result_mul}")

# Equality comparison
print(f"Equality: {c1} == {c2} is {c1.equal(c2)}")

# Inequality comparison
print(f"Inequality: {c1} != {c2} is {c1.not_equal(c2)}")
