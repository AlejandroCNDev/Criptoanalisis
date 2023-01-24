
import time
import numpy as np
import math

def fermat(n):
    A = math.ceil(math.sqrt(n))
    B = pow(A, 2) - n

    while not (math.isqrt(B) ** 2 == B):  # while B no sea un cuadrado perfecto:
        A = A + 1
        B = pow(A, 2) - n

    return [int(A - math.sqrt(B)), int(A + math.sqrt(B))]


with open("ExtensionRetosFactorizacion.txt", "r") as f:
    lines = f.readlines()

num_40 = []
num_44 = []
num_48 = []
num_52 = []
num_56 = []
num_60 = []
num_64 = []
num_68 = []
num_72 = []
num_76 = []
num_80 = []
num_92 = []
num_104 = []
num_116 = []
num_128 = []

for line in lines:
    if line.strip() == "" or line.startswith("#"):
        continue
    try:
        t, n = line.strip().split(",")
        t = int(t.strip())
        n = int(n.strip())
        if t == 40:
            num_40.append(n)
        elif t == 44:
            num_44.append(n)
        elif t == 48:
            num_48.append(n)
        elif t == 52:
            num_52.append(n)
        elif t == 56:
            num_56.append(n)
        elif t == 60:
            num_60.append(n)
        elif t == 64:
            num_64.append(n)
        elif t == 68:
            num_68.append(n)
        elif t == 72:
            num_72.append(n)
        elif t == 76:
            num_76.append(n)
        elif t == 80:
            num_80.append(n)
        elif t == 92:
            num_92.append(n)
        elif t == 104:
            num_104.append(n)
        elif t == 116:
            num_116.append(n)
        elif t == 128:
            num_128.append(n)

    except ValueError:
        print(f"Line {line} is not in the expected format")

print(num_40)
print(num_44)
print(num_48)
print(num_52)
print(num_56)
print(num_60)
print(num_64)
print(num_68)
print(num_72)
print(num_76)
print(num_80)
print(num_92)
print(num_104)
print(num_116)
print(num_128)

"""
for i in num_40:
    print(fermat(i))
for i in num_44:
    print(fermat(i))
for i in num_48:
    print(fermat(i))
for i in num_52:
    print(fermat(i))
"""


times_experiments = []

print("#################################################################")
print("#################################################################")
print("#################################################################\n")

for i in num_76[:1]:
    print("#################################################################")
    print("######################" + " Experimento " + str(i) + " ############################\n")

    # Para calcular el tiempo de ejecución
    ini_time = time.time()

    print(fermat(i))

    fin_time = time.time()
    timeOneExperiment = fin_time - ini_time
    times_experiments.append(timeOneExperiment)
    print("\nEl tíempo de ejecución del programa " + str(timeOneExperiment) + "\n")

print("#################################################################")
print("La media obtenida de los experimentos es: " + str(np.average(times_experiments)))
print("La varianza obtenida de los experimentos es: " + str(np.var(times_experiments)))
print("La desviación tipica obtenida de los experimentos es: " + str(np.std(times_experiments)))

