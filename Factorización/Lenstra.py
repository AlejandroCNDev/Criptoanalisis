"""Require: Un número entero positivo compuesto n
Ensure: Un factor primo de n
1: Fijar cota B // Suponer que el orden de la curva es B-smooth
2: Escoger una CE módulo n cualquiera y
2 = x
3 + ax + b mod n.
3: Escoge un punto cualquiera de la curva P = (x0, y0)
4: k = 2
5: while k ≤ B do
6: Obtener P = kP mod n
7: if es posible then k + + else Hemos encontrado un t tal
que mcd(t, n) = d y podemos return d end if
8: end while
9: if k > B then Probar con otra curva y otro punto inicial end if
"""
"""
import math
import random

def lenstra(n):
    # Inicializamos el conjunto de factores.
    factors = set()

    # Repetimos el proceso hasta que no quede ningún factor por encontrar.
    while n > 1:
        # Seleccionamos un valor aleatorio para a.
        a = random.randint(2, n - 1)

        # Inicializamos los valores de x y y.
        x = y = 1
        d = 1

        # Iteramos hasta que encontremos un factor o hasta que
        # alcancemos el límite de pasos permitido.
        while d == 1:
            # Calculamos el siguiente valor de x.
            x = (x * x + 1) % n

            # Calculamos el siguiente valor de d.
            d = math.gcd(abs(x - y), n)

            # Si d es divisible por n, entonces no hemos encontrado
            # un factor y debemos volver a empezar.
            if d == n:
                break

        # Si d es un factor, entonces lo añadimos al conjunto.
        if d > 1:
            factors.add(d)

        # Actualizamos el valor de n.
        n //= d

    # Devolvemos el conjunto de factores.
    return factors


# Ejemplo de uso
n = 2534
print(lenstra(n))  # Imprime {2, 3, 3, 5, 3607, 3803}
"""

"""
import random

def lenstra(curve, alpha, beta):
    # Check if curve is a valid elliptic curve
    if not isinstance(curve, EllipticCurve):
        raise TypeError("curve must be an EllipticCurve")

    # Check if alpha and beta are elements of the curve's group
    if alpha not in curve.group or beta not in curve.group:
        raise ValueError("alpha and beta must be elements of the curve's group")

    # Find a random quadratic nonresidue x
    x = random.randint(2, curve.p-1)
    while curve.is_quadratic_residue(x):
        x = random.randint(2, curve.p-1)

    # Initialize variables
    c = random.randint(1, curve.p-1)
    y = x
    r = 1
    v = (curve.p+1)//2

    # Loop until r is not 1
    while r == 1:
        x = x**2 % curve.p
        r = gcd(y - x, curve.p)
        if r > 1:
            break

        v = (v+1) % curve.p
        if v == 0:
            y = x
            v = (curve.p+1)//2

    # Compute the discrete logarithm using the Shanks-Tonelli algorithm
    if r == curve.p:
        return None
    else:
        return shanks_tonelli(curve, alpha, beta, r)

# Define the elliptic curve y^2 = x^3 + ax + b mod p
p = 223
a = 0
b = 7
curve = EllipticCurve(p, a, b)

# Choose an element alpha of the curve's group
alpha = Point(192, 105, curve)

# Choose an integer beta such that alpha^beta is the element for which we want to find the discrete logarithm
beta = 2

# Find the discrete logarithm using the Lenstra algorithm
result = lenstra(curve, alpha, beta)
print(result)  # prints 3
"""
import argparse
from random import randint
from math import gcd


# Sieve of Eratosthenes
def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            for i in range(p, n + 1, p):
                b[i] = False
    return ps


# Finds modular inverse
# Returns inverse, unused helper and gcd
def modular_inv(a, b):
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = modular_inv(b, r)
    return y, x - q * y, g


# Addition in Elliptic curve modulo m space
def elliptic_add(p, q, a, b, m):
    # If one point is infinity, return other one
    if p[2] == 0: return q
    if q[2] == 0: return p
    if p[0] == q[0]:
        if (p[1] + q[1]) % m == 0:
            return 0, 1, 0  # Infinity
        num = (3 * p[0] * p[0] + a) % m
        denom = (2 * p[1]) % m
    else:
        num = (q[1] - p[1]) % m
        denom = (q[0] - p[0]) % m
    inv, _, g = modular_inv(denom, m)
    # Unable to find inverse, arithmetic breaks
    if g > 1:
        return 0, 0, denom  # Failure
    z = (num * inv * num * inv - p[0] - q[0]) % m
    return z, (num * inv * (p[0] - z) - p[1]) % m, 1


# Multiplication (repeated addition and doubling)
def elliptic_mul(k, p, a, b, m):
    r = (0, 1, 0)  # Infinity
    while k > 0:
        # p is failure, return it
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = elliptic_add(p, r, a, b, m)
        k = k // 2
        p = elliptic_add(p, p, a, b, m)
    return r


# Lenstra's algorithm for factoring
# Limit specifies the amount of work permitted
def lenstra(n, limit):
    g = n
    while g == n:
        # Randomized x and y
        q = randint(0, n - 1), randint(0, n - 1), 1
        # Randomized curve coefficient a, computed b
        a = randint(0, n - 1)
        b = (q[1] * q[1] - q[0] * q[0] * q[0] - a * q[0]) % n
        g = gcd(4 * a * a * a + 27 * b * b, n)  # singularity check
    # If we got lucky, return lucky factor
    if g > 1:
        return g
    # increase k step by step until lcm(1, ..., limit)
    for p in primes(limit):
        pp = p
        while pp < limit:
            q = elliptic_mul(p, q, a, b, n)
            # Elliptic arithmetic breaks
            if q[2] > 1:
                return gcd(q[2], n)
            pp = p * pp
    return False


# Command line tool
def main():
    parser = argparse.ArgumentParser(description = 'Process arguments')
    parser.add_argument('--n', type = int, help = 'number to factor')
    parser.add_argument('--limit', type = int, default = 1000, help = 'work limit (default = 1000)')
    args = parser.parse_args()
    print(lenstra(args.n, args.limit))

if __name__ == '__main__':
    main()