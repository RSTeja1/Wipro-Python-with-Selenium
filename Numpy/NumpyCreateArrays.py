

#Using numpy.ones()
#Using numpy.zeros()
#using numpy.arange() function
#using numpy.linespace() function
#using numpy.random.rand() function
#using numpy.empty() function
#using numpy.full() function

import numpy as np
from numpy.ma.core import identity

#1D array
#this function creates a Numpy array filled with waters
a = np.zeros(5)
print(a)

#2D array
a_2D = np.zeros((4,3))
print(a_2D)

#Using numpy.ones()
a = np.ones(5)
print(a)

#2D array
a_2D = np.ones((4,3))
print(a_2D)

#using numpy.arange() function

#with only the stop
a = np.arange(10)
print(a)

#providing the start, step and stop values
a = np.arange(1,10,2)
print(a)

#using numpy.linespace() function
#includes the last number
a = np.linspace(0,10,num =5, endpoint= True)
print(a)

#exclude the last number
a = np.linspace(0,10,num =5, endpoint= False)
print(a)

#using numpy.random.rand() function
a = np.random.rand(5)
print(a)

#2D
a = np.random.rand(2,3)
print(a)

#3D
a = np.random.rand(2,3,4)
print(a)

#using numpy.empty() function
#2D
a = np.empty((2,3))
print(a)

#using numpy.full() function
a = np.full((2,3), 5)
print(a)

#numpy.eye()
identity_matrix = np.eye((4))
print(identity_matrix)

#numpy.identity - function is used generate a square identity matrix
identity_matrix = np.identity((5))
print(identity_matrix)

#numpy.diag()
#in case of 2D array, the function extracts the diagnol elements of array

Matrix = np.array([[10, 20, 30],[40, 50, 60], [70, 80, 90]])
print("Original matrx" ,Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)

