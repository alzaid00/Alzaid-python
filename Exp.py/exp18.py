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




import numpy as np

one_d_array = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(one_d_array)

print("\nSlicing 1D array (Index 1 to 3):")
print(one_d_array[1:4])

reshaped_2d = one_d_array.reshape(1, 5) 
print("\nReshaped 1D Array to 2D (1x5):")
print(reshaped_2d)

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(two_d_array)

print("\nSlicing 2D array (First 2 rows, all columns):")
print(two_d_array[:2, :])

reshaped_3d = two_d_array.reshape(1, 3, 3)  
print("\nReshaped 2D Array to 3D (1x3x3):")
print(reshaped_3d)

three_d_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3D Array:")
print(three_d_array)

print("\nAccessing 3D Array Element (First block, first row, second column):")
print(three_d_array[0, 0, 1])  

print("\nSlicing 3D Array (First block):")
print(three_d_array[0])
