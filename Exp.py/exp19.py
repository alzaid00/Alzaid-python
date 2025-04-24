#14.	Develop a Python script to create two arrays of the same shape and perform element-wise addition, subtraction, multiplication, and division. Calculate the dot product and cross product of two vectors.


# Name: Alzaid khan DIV: E(ECS)
# UIN: 241S009  Roll no. 09
import numpy as np
# Create two arrays of the same shape
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
addition = np.add(array1, array2)
print("Element-wise Addition:")
print(addition)

# Element-wise subtraction
subtraction = np.subtract(array1, array2)
print("\nElement-wise Subtraction:")
print(subtraction)

# Element-wise multiplication
multiplication = np.multiply(array1, array2)
print("\nElement-wise Multiplication:")
print(multiplication)

# Element-wise division
division = np.divide(array1, array2)
print("\nElement-wise Division:")
print(division)

# Dot product of the two vectors
dot_product = np.dot(array1, array2)
print("\nDot Product:")
print(dot_product)

# Cross product of the two vectors
cross_product = np.cross(array1, array2)
print("\nCross Product:")
print(cross_product)





import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

print("--- Element-wise Operations ---")

addition = array1 + array2
print("Addition:")
print(addition)

subtraction = array1 - array2
print("\nSubtraction:")
print(subtraction)

multiplication = array1 * array2
print("\nMultiplication:")
print(multiplication)

try:
    division = array1 / array2
    print("\nDivision:")
    print(division)
except ZeroDivisionError:
    print("Error: Division by zero.")

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

print("\n--- Dot and Cross Product ---")

dot_product = np.dot(vector1, vector2)
print("Dot Product:")
print(dot_product)

cross_product = np.cross(vector1, vector2)
print("\nCross Product:")
print(cross_product)
