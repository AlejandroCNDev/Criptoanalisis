from math import gcd
from random import randint


def pollard_kangaroo(g, h, p):
    x = y = randint(0, p - 1)
    fx = fy = pow(g, x, p)
    k = 1
    while True:
        x = (pow(g, k, p) * fx) % p
        y = (pow(g, 2 * k, p) * fy) % p
        if x == y:
            return None
        fx = pow(g, k, p) * fx % p
        fy = pow(g, 2 * k, p) * fy % p
        k += 1
        d = gcd(abs(x - y), p)
        if d > 1:
            if d == p:
                return None
            else:
                log = (x - y) // d
                if pow(g, log, p) == h:
                    return log
                else:
                    return None

print(pollard_kangaroo(3, 8, 11))
