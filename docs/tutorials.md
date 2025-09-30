In this example we compute
$$
I=\int_{1}^{3}(x^6 - x^2\sin(2x))dx
$$
using Gaussian quadrature with Legendre polynomials.


import numpy as np

# Function to compute Gauss–Legendre nodes and weights
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

# Function to scale nodes and weights
def gaussxwab(a, b, x, w):
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

# Function to integrate
def fInt(x):
    return (x**6) - (x**2 * np.sin(2*x))

# Example: compute with N=4
x4, w4 = gaussxw(4)
x4Esc, w4Esc = gaussxwab(1.0, 3.0, x4, w4)
I4 = np.sum(w4Esc * fInt(x4Esc))
print("Result with N=4:", I4)
```
