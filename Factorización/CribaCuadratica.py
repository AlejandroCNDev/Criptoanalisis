"""Require: Un número entero positivo compuesto n
Ensure: Un factor de n
1: B = {p1, p2, p3, . . . , pk} base de factores primos pequeños
2: m = ⌊√n⌋
3: repeat
4: Considera ti en el orden 0, ±1, ±2 . . .
5: a = (m + ti)
6: b = (m + ti)
2 − n //Valores cercanos a 0
7: if b es factorizable en B then
8: ai = a; bi = b
9: vi = exponentes de la factorización de bi
10: end if
11: until Se hayan considerado suficientes valores vi
12: loop
13: Encontrar vectores ⟨v1, v2 . . . vq⟩ cuya suma resulte en un vector
(sv) con todos los componentes pares
14: x =
∏
1≤i≤q
asv[i]
15: y =
∏
1≤i≤k
p
sv[i]/2
i
16: if x ≡ ±y (mod n) then buscar otro conjunto de vectores end if
17: return mcd(x − y, n)
18: end loop"""


"""
def criba_cuadratica(n):
    # Crea una lista de números del 2 al n
    numeros = list(range(2, n + 1))

    # Recorre la lista de números y elimina sus múltiplos
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[j] % numeros[i] == 0:
                numeros.pop(j)

    # Devuelve la lista de números que quedan, que son los números primos
    return numeros


# Prueba el algoritmo con el número 20

print(criba_cuadratica(20))  # debería imprimir [2, 3, 5, 7, 11, 13, 17, 19]
"""

"""
def criba_cuadratica(n):
    if n < 2:
        return []
    # Tomamos n como el límite superior para la criba
    l = [i for i in range(2, n+1)]
    # Inicializamos la lista de factores primos encontrados
    p = []
    while len(l) > 0:
        # Tomamos el primer elemento de la lista como el siguiente número primo
        p.append(l[0])
        # Eliminamos todos los múltiplos del número primo encontrado
        l = [x for x in l if x % p[-1] != 0]
    return p

# Probamos la función con un número grande
print(criba_cuadratica(6557))
"""



def criba_eratostenes(n):
    if n < 2:
        return []
    # Tomamos n como el límite superior para la criba
    l = [i for i in range(2, n+1)]
    # Inicializamos la lista de factores primos encontrados
    p = []
    while len(l) > 0:
        # Tomamos el primer elemento de la lista como el siguiente número primo
        p.append(l[0])
        # Eliminamos todos los múltiplos del número primo encontrado
        l = [x for x in l if x % p[-1] != 0]
    return p

# Probamos la función con un número pequeño
#print(criba_eratostenes(2534389177))

def quadratic_sieve(n):
    primes = []
    is_composite = [False] * (n+1)
    for i in range(2, int(n**(1/2))+1):
        if not is_composite[i]:
            primes.append(i)
            for j in range(i**2, n+1, i):
                is_composite[j] = True
    for i in range(int(n**(1/2))+1, n+1):
        if not is_composite[i]:
            primes.append(i)
    return primes

print(quadratic_sieve(10579))

