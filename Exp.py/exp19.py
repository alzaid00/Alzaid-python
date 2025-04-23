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
