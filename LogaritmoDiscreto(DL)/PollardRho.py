"""import numpy as numpy

#Pollard-Rho

p = 5
o = 1

# 1: a = b = aa = bb = 0; i = x = xx = 1
a = b = aa = bb = 0
i = x = xx = 1

while(i < p):
    x = f(x, a, b, p, o)
    xx = f(xx, aa, bb, p, o)
    xx = f(xx, aa, bb, p, o)
    if x == xx:
        if numpy.gcd(b-bb,o) != 1
            return False
        return (aa-a)*(pow(b-bb,-1,o))
return False

"""

import math
import time


# ALGORITMO POLLARD-RHO PARA EL CÁLCULO DEL LOGARITMO DISCRETO

# Comprobación
def isCorrect(beta, alfa, t, p):
    bool = False
    if (beta == pow(alfa, t, p)):
        bool = True
    else:
        bool
    return bool


# Algoritmo Extendido de Euclides
def EuclidesExt(a, b):
    if (b == 0):
        return a, 1, 0
    else:
        dd, xx, yy = EuclidesExt(b, a % b)
        d = dd
        x = yy
        y = xx - math.floor(a / b) * yy

    return d, x, y


# Función para calcular la operación para obtener los valores
def f(x, a, b, alfa, beta, p):
    condition = x % 3

    if (condition == 0):
        x = pow(x, 2, p)
        a = (2 * a) % (p - 1)
        b = (2 * b) % (p - 1)
    elif (condition == 1):
        x = (beta * x) % p
        a = a
        b = (b + 1) % (p - 1)
    elif (condition == 2):
        x = (alfa * x) % p
        a = (a + 1) % (p - 1)
        b = b

    return x, a, b


def pollardRho(alfa, beta, p, o):
    # # 1: a = b = aa = bb = 0; i = x = xx = 1
    # a = b = aa = bb = 0
    # i = x = xx = 1
    i = x = xx = 1
    a = b = aa = bb = 0
    o = o  # Orden de un subgrupo multiplicativo

    #while (i < p):
    while i < p:
        i += 1
        # One step
        # x = f(x, a, b, p, o)
        x, a, b = f(x, a, b, alfa, beta, p)

        # xx = f(xx, aa, bb, p, o)
        # xx = f(xx, aa, bb, p, o)

        # Two steps
        xx, aa, bb = f(xx, aa, bb, alfa, beta, p)
        xx, aa, bb = f(xx, aa, bb, alfa, beta, p)

        #if x == xx:
        if (x == xx):

            if (math.gcd(b - bb, o) != 1):
                return False

            inverso = EuclidesExt(b - bb, o)[1]
            if (inverso < 0):
                inverso += o

            return ((aa - a) * inverso) % o
    return False


# Ejemplo
inicio = time.time()
alfa = 9
beta = 804
p = 853
o = 71


# 	 n <entero>: Taman~o del problema (en bits)
# 	 p <entero>: valor del mo'dulo
# 	 alpha <entero>: generador considerado
# 	 beta <entero>: resultado de a^t mod p
# 	 o <entero>: orden del grupo generado por alpha
#

# Solucion x

x = pollardRho(alfa, beta, p, o)

print("Valor de x es: ", x, "\n")

fin = time.time()
print("¿Es correcto? ", isCorrect(beta, alfa, x, p))
print("El tiempo de ejecucion del programa es: ", fin - inicio, "segundos.")