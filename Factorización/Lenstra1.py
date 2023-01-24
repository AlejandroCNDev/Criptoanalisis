import random
import math

def lenstra(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    if n == 1:
        return factors
    while n != 1:
        x = random.randint(1, n-1)
        y = random.randint(1, n-1)
        g = 1
        m = 1
        while g == 1:
            x = ((x*x + y) % n)
            y = ((x*x + y*y) % n)
            g = math.gcd(abs(x - y), n)
            m += 1
        if g == n:
            while True:
                x = ((x*x + y) % n)
                y = ((x*x + y*y) % n)
                g = math.gcd(abs(x - y), n)
                if g > 1:
                    break
        n = n // g
        factors.append(g)
    return factors

print(lenstra(6407))