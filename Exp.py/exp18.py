# 13.	Write a Python program to create a 1D, 2D, and 3D NumPy array. Perform basic operations like reshaping, slicing, and indexing.

# Name: Alzaid khan DIV: E(ECS)
# UIN: 241S009  Roll no. 09
import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])

print(" 1D Array:")

print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]]) 
print("\n 2D Array:") 
print(array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 
print("\n 3D Array:")

print(array_3d)

reshaped = np.arange(12).reshape(3, 4) 
print("\n Reshaped Array (3x4):") 
print(reshaped)

print("\n Indexing [2] from 1D Array:", array_1d[2])

print(" Indexing [1, 2] from 2D Array:", array_2d [1, 2])

print(" Indexing [1, 0, 1] from 3D Array:", array_3d[1, 0 , 1])

print("\n Slicing 1D Array [1:4]:", array_1d[1:4])

print(" Slicing 2D Array [0, 1:3]:", array_2d[0, 1:3])

print(" Slicing 3D Array [0, 1]:", array_3d[0, :, 1])
