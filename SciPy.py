# Scipy is a powerful open-source library for scientific computing and technical computing in Python
# It builds on top of Numpy and provides additional functionality for various scientific and engineering applications. 
# Scipy offers a wide range of modules and sub-packages that cover different areas, including optimization, interpolation, integration, linear algebra, signal processing, image processing, statistics, and more

# Here is an overview, brief explanation, and an example for some of the key packages in Scipy

# 1. scipy.optimize: This package provides functions for optimization problems, including root finding, least-squares fitting, and minimization of scalar functions. 
# It offers several optimization algorithms for different problem types
from scipy.optimize import minimize

def objective(x):
    return x ** 2 + 3 * x + 4

# Use the 'minimize' function from scipy.optimize to find the minimum of the objective function.
# Starting from x0=0, the 'Nelder-Mead' method is used for optimization.
result = minimize(objective, x0=0, method='Nelder-Mead')

# Print the optimized value of x.
print("Optimized value:", result.x)

# 2. scipy.interpolate: This package offers various interpolation techniques to estimate values between known data points. 
# It provides functions for 1-D and multi-dimensional interpolation, spline interpolation, and smoothing splines.
import numpy as np
from scipy.interpolate import CubicSpline

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 1, 6, 8])

# Create a cubic spline interpolation object using the given data points (x, y).
interp = CubicSpline(x, y)

new_x = 3.5

# Interpolate the value at new_x using the cubic spline.
interpolated_value = interp(new_x)

# Print the interpolated value at new_x.
print("Interpolated value at x =", new_x, ":", interpolated_value)

# 3. scipy.integrate: This package provides functions for numerical integration and solving differential equations. 
# It offers methods for integrating ordinary differential equations (ODEs) and solving initial value problems.
from scipy.integrate import quad

def f(x):
    return x ** 2

result, error = quad(f, 0, 1)
print("Result:", result)
print("Error:", error)

# 4. scipy.linalg: This package provides functions for linear algebra operations, such as matrix decompositions, solving linear systems, eigenvalue computations, and more
import numpy as np
from scipy.linalg import eig

A = np.array([[1, 2], [3, 4]])

eigenvalues, eigenvectors = eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# 1. scipy.cluster
# Clustering algorithms are useful in information theory, target detection, communications, compression, and other area

# 2. scipy.constants
# Physical and mathematical constants and units.
# Examples include: pi, Avogadro(Avogadro Constant), quetta (10^30), tera(10^12)

# 3. scipy.datasets
# Loads SciPy datasets
# Examples include: ascent(), face([gray])

# View additional submodules on: https://docs.scipy.org/doc/scipy/reference/main_namespace.html#


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from scipy.optimize import minimize

# Define the function to minimize
def f(x):
    return (x - 3)**2

# Perform the minimization using the minimize function from scipy.optimize
res = minimize(f, 2)

# Print the optimal value of x that minimizes the function
print(res.x)

# Print the result object which contains additional information
print(res)
