#!/usr/bin/env python3

import numpy as np





#Para la sección dos, la página web será la siguiente:
# https://oisao.github.io/Gaussian_Cuadrature/



#¿Con cuál valor de N se alcanza el resultado exacto?
#Según la teoría de la cuadratura Gaussiana, debería de ser 2N-1 que en este caso sería 2*2-1 = 4. Pero note que cuando se hacen las pruebas, entre mayor el N, más se acerca a una aproximación. Pero la diferencia en este caso, es la función seno. Esta no es un polinomio, entonces la parte x^2 sin(2x) no es un polinomio. Como la condición 2N-1 solo se garantiza para polinomios, es por esto que NO es uno exacto, sino que entre mayor más se "aproxima". 


#Función que devuelve pesos y puntos de colocación
def gaussxw(N):
    """
    Compute Gauss–Legendre nodes and weights on [-1, 1].

    Args:
        N (int): Number of quadrature points.

    Returns:
        tuple: A tuple (x, w) where
            - x (ndarray): Nodes of the quadrature rule.
            - w (ndarray): Corresponding weights.

    Examples:
        >>> x, w = gaussxw(3)
        >>> len(x), len(w)
        (3, 3)
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    """
    Scale nodes and weights from the interval [-1, 1] to [a, b].

    Args:
        a (float): Left endpoint of the interval.
        b (float): Right endpoint of the interval.
        x (ndarray): Nodes on [-1, 1].
        w (ndarray): Weights on [-1, 1].

    Returns:
        tuple: A tuple (x_scaled, w_scaled) where
            - x_scaled (ndarray): Scaled nodes in [a, b].
            - w_scaled (ndarray): Scaled weights for [a, b].

    Examples:
        >>> x, w = gaussxw(2)
        >>> x_s, w_s = gaussxwab(1, 3, x, w)
        >>> len(x_s), len(w_s)
        (2, 2)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

#Función a integrar

def funcInt(x):
    """
    Integrand function: f(x) = x^6 - x^2 * sin(2x).

    Args:
        x (float or ndarray): Input values.

    Returns:
        float or ndarray: The function evaluated at x.

    Examples:
        >>> funcInt(1.0)
        1.0 - np.sin(2.0)
    """
    return (x ** 6) - (x ** 2 * np.sin(2 * x))

# N = 2
x2, w2 = gaussxw(2)

# N = 3
x3, w3 = gaussxw(3)

# N = 4
x4, w4 = gaussxw(4)

# N = 5
x5, w5 = gaussxw(5)

# N = 6
x6, w6 = gaussxw(6)

# N = 7
x7, w7 = gaussxw(7)

# N = 8
x8, w8 = gaussxw(8)

# Escalar los nodos y pesos
x2Esc, w2Esc = gaussxwab(1, 3, x2, w2)
x3Esc, w3Esc = gaussxwab(1, 3, x3, w3)
x4Esc, w4Esc = gaussxwab(1, 3, x4, w4)
x5Esc, w5Esc = gaussxwab(1, 3, x5, w5)
x6Esc, w6Esc = gaussxwab(1, 3, x6, w6)
x7Esc, w7Esc = gaussxwab(1, 3, x7, w7)
x8Esc, w8Esc = gaussxwab(1, 3, x8, w8)

# Evaluar la integral para cada N
func2 = np.sum(w2Esc * funcInt(x2Esc))
print(func2)

func3 = np.sum(w3Esc * funcInt(x3Esc))
print(func3)

func4 = np.sum(w4Esc * funcInt(x4Esc))
print(func4)

func5 = np.sum(w5Esc * funcInt(x5Esc))
print(func5)

func6 = np.sum(w6Esc * funcInt(x6Esc))
print(func6)

func7 = np.sum(w7Esc * funcInt(x7Esc))
print(func7)

func8 = np.sum(w8Esc * funcInt(x8Esc))
print(func8)

