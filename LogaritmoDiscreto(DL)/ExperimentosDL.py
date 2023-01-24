import time
import numpy as np
import math

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
def func(x, a, b, alfa, beta, p):
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
        x, a, b = func(x, a, b, alfa, beta, p)

        # xx = f(xx, aa, bb, p, o)
        # xx = f(xx, aa, bb, p, o)

        # Two steps
        xx, aa, bb = func(xx, aa, bb, alfa, beta, p)
        xx, aa, bb = func(xx, aa, bb, alfa, beta, p)

        #if x == xx:
        if (x == xx):

            if (math.gcd(b - bb, o) != 1):
                return False

            inverso = EuclidesExt(b - bb, o)[1]
            if (inverso < 0):
                inverso += o

            return ((aa - a) * inverso) % o
    return False


"""
def baby_step_giant_step(primo, alpha, beta):
    # 1:n = ⌈√p⌉
    n = math.ceil(math.sqrt(primo))

    T = {}

    # Creamos un diccionario para almacenar los pasos baby.
    for r in range(n-1):
        #Almacena en T el par ⟨r, αr mod p⟩ indexado por α r mod p
        T[pow(alpha, r, primo)] = r

    # Calcula alpha^(−n) mod p y asigna gamma = β

    # Giant Step Precomputation via Fermat's Little Theorem
    # (This implies that alpha**(p-2) (mod p) is the inverse of alpha)
    c = pow(alpha, n*(primo-2), primo) # c = alpha^(-n) mod p

    # Search for an equivalence in the table. Giant step.
    for q in range(n-1):
        # γ = γ*α^(−n) mod p
        gamma = (beta * pow(c, q, primo)) % primo
        #Si el término gigante se encuentra en el diccionario,
        #entonces hemos encontrado la solución.
        if gamma in T: # Existe un par {r, gamma}
            return q * n + T[gamma]

    # Si llegamos aquí, entonces no hemos encontrado la solución.
    return None
"""

with open("ExtensionRetosDL.txt", "r") as f:
    lines = f.readlines()

num_32 = []
num_36 = []
num_40 = []
num_44 = []
num_48 = []
num_52 = []
num_56 = []
num_60 = []
num_64 = []
num_80 = []
num_96 = []
num_112 = []
num_128 = []

for line in lines:
    if line.strip() == "" or line.startswith("#"):
        continue
    try:
        n, p, alpha, beta, orden = line.strip().split(",")
        n = int(n.strip())
        p = int(p.strip())
        alpha = int(alpha.strip())
        beta = int(beta.strip())
        orden = int(orden.strip())

        if n == 32:
            num_32.append([p, alpha, beta, orden])
        elif n == 36:
            num_36.append([p, alpha, beta, orden])
        elif n == 40:
            num_40.append([p, alpha, beta, orden])
        elif n == 44:
            num_44.append([p, alpha, beta, orden])
        elif n == 48:
            num_48.append([p, alpha, beta, orden])
        elif n == 52:
            num_52.append([p, alpha, beta, orden])
        elif n == 56:
            num_56.append([p, alpha, beta, orden])
        elif n == 60:
            num_60.append([p, alpha, beta, orden])
        elif n == 64:
            num_64.append([p, alpha, beta, orden])
        elif n == 80:
            num_80.append([p, alpha, beta, orden])
        elif n == 96:
            num_96.append([p, alpha, beta, orden])
        elif n == 112:
            num_112.append([p, alpha, beta, orden])
        elif n == 128:
            num_128.append([p, alpha, beta, orden])

    except ValueError:
        print(f"Line {line} is not in the expected format")

print(num_32)
print(num_36)
print(num_40)
print(num_44)
print(num_48)
print(num_52)
print(num_56)
print(num_60)
print(num_64)
print(num_80)
print(num_96)
print(num_112)
print(num_128)



times_experiments = []

print("#################################################################")
print("#################################################################")
print("#################################################################\n")
for i in num_32:
    print("#################################################################")
    print("######################" + " Experimento " + str(i) + " ############################\n")

    # Para calcular el tiempo de ejecución
    ini_time = time.time()

    alfa = i[1]
    beta = i[2]
    p = i[0]
    o = i[3]
    print(pollardRho(alfa,beta,p,o))

    fin_time = time.time()
    timeOneExperiment = fin_time - ini_time
    times_experiments.append(timeOneExperiment)
    print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

print("#################################################################")
print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))