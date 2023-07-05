# Numpy Library

# Numpy is a powerfuö library for scientific computing in Python
# It stands for "Numerical Python"
# It provides a wide range of functionalities for working with large, multi-dimensional arrays and matrices along with mathematical functions to operate on arrays efficiently

# Some of the functions that maybe used with Numpy include:

# 1. ndarray - an efficient multidimensional array providing fast array-oriented arithmetic operations and flexible broadcasting capabilities
# 2. Mathematical functions for fast operations on entire arrays of data without having to write loops
# 3. Tools for reading / writing array data on disk and working with memory-mapped files
# 4. Linear Algebra, random number generation and Fourier transform capabilities
# 5. A C API for connecting NumPy with libraries in C, C++, FORTRAN

# Basic Calculations you can perform with NumPy

# 1. Addition
import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = a + b
print(c)

# 2. Subtraction
import numpy as np
a = np.array([10, 9, 8, 7, 6])
b = np.array([1, 2, 3, 4, 5,])
c = a - b
print(c)

# 3. Multiplication
import numpy as np
a = np.array([2, 4, 6])
b = np.array([10, 100, 1000])
c = a*b
print(c)

# 4. Division
import numpy as np
a = np.array([27, 64, 81])
b = np.array([9, 16, 3])
c = a / b
print(c)


# Mathematical Functions

# 5. Exponential
import numpy as np
a = np.array([1, 2, 3])
b = np.exp(a)
print(b)

# 6. Square root
import numpy as np
a = np.array([4, 9, 16])
b = np.sqrt(a)
print(b)  

# 7. Trignometric Funtions
import numpy as np
a = np.array([30, 45, 60])
b = np.sin(a)
print(b)

# 8. Mean
import numpy as np
a = np.array([20, 30, 70])
mean = np.mean(a)
print(mean)

# 9. Median
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7])
median = np.median(a)
print(median)

# 10. Mode
import numpy as np
from scipy.stats import mode
a = np.array([1, 2, 2, 3, 4, 4, 4])
mode_value = mode(a)
print(mode_value)  
  

# 11. Absolute Value
import numpy as np
a = np.array([-2, 4, -6, 8])
abs_values = np.abs(a)
print(abs_values) 

# 12. Square
import numpy as np
a = np.array([2, 3, 4])
square_values = np.square(a)
print(square_values) 

# 13. Natural Logarithm
import numpy as np
a = np.array([1, 10, 100])
log_values = np.log(a)
print(log_values) 

# 14. Base-10 Logarithm
import numpy as np
a = np.array([10, 100])
log_values = np.log10(a)
print(log_values)

# 15. Modf: Return the fractional and integral parts of each element as separate arrays
import numpy as np
a = np.array([-1.5, 2.7, 3.2])
fractional, integral = np.modf(a)
print(fractional)  
print(integral) 

# 16. IsNaN: Check if each value is NaN (Not a Number
import numpy as np
a = np.array([1, np.nan, 3, 0]) 
is_nan_values = np.isnan(a)
print(is_nan_values)

# 17. IsFinite: Check if each element is finite (non-inf, non-NaN)
import numpy as np
a = np.array([4, 6, np.nan])
is_finite_values = np.isfinite(a)
print(is_finite_values)

# 18. IsInf: Check if each element is infinite
import numpy as np
a = np.array([5, np.inf])
infinite_values = np.isinf(a)
print(infinite_values)

# 19. Trigonometric Functions
import numpy as np

angles = np.array([0, np.pi/2, np.pi, 180, 90, 60])
cos_values = np.cos(angles)
sin_values = np.sin(angles)
tan_values = np.tan(angles)

print(cos_values)  
print(sin_values) 
print(tan_values)  

# 20. Shape: The shape of an array in NumPy is represented by a tuple of integers that specifies the size of each dimension
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)

# 21. Reshape: The reshape() function in NumPy allows you to change the shape of an array without modifying its elements
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)

# 22. Linspace: numpy.linspace() is a function that generates an array of evenly spaced values over a specified range.
import numpy as np
arr = np.linspace(0, 1, 5)
print(arr)

# 23. Range printing: Range printing refers to generating a sequence of values within a specified range
# Using range() and list()
arr = list(range(1, 6))
print(arr)
# Using numpy.arange()
import numpy as np
arr = np.arange(1, 6)
print(arr)

# 24. Ravel: numpy.ravel() is a function that flattens a multi-dimensional array into a 1-dimensional array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
raveled_arr = np.ravel(arr)
print(raveled_arr)

# 25. Sum axis: In NumPy, axis refers to the dimension along which a particular operation is performed
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
sum_axis_0 = np.sum(arr, axis=0)
print(sum_axis_0)

sum_axis_1 = np.sum(arr, axis=1)
print(sum_axis_1)






