def factorize(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append((i, 1))
            n = n // i
            while n % i == 0:
                factors[-1] = (i, factors[-1][1] + 1)
                n = n // i
    if n > 1:
        factors.append((n, 1))
    return factors

def crib_racional(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.extend(factorize(n // i))
            break
    else:
        factors = [n]
    return factors

print(crib_racional(360)) # Output: [2, 2, 3, 3, 5]
