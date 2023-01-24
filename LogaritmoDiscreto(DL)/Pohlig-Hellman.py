def pohlig_hellman(g, h, p):
    phi = p - 1
    factors = factorize(phi)
    result = []
    for pi, ei in factors:
        gi = pow(g, phi // pi, p)
        hi = pow(h, phi // pi, p)
        mi = discrete_log_mod_prime_power(gi, hi, pi, ei)
        result.append((pi, mi))
    return result

def discrete_log_mod_prime_power(g, h, p, e):
    ge = pow(g, p ** (e - 1), p ** e)
    he = pow(h, p ** (e - 1), p ** e)
    table = {he * pow(g, j, p ** e): j for j in range(p)}
    for i in range(1, e):
        x = pow(ge, p ** i, p ** e)
        if x in table:
            return i * p + table[x]
    return None

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

print(pohlig_hellman(3, 8, 11))
