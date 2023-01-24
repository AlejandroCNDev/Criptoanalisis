def div_tentativa(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return factors

print(div_tentativa (360)) # Output: [2, 2, 3, 3, 5]
