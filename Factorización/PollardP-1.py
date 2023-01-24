# Require: Un número entero positivo compuesto n
# Ensure: Un factor de n
import time

import math, random

# Require: Un número entero positivo compuesto n
# Ensure: Un factor de n
def pollard_P_1(n):
    # 1: Escoger A aleatorio tal que 2 ≤ A ≤ n − 1
    A = random.randint(2,n-1)

    if 1 < math.gcd(A, n) < n:
        return math.gcd(A, n)

    k = 2

    while True:
        A = pow(A, k, n)
        d = math.gcd(A - 1, n)
        if 1 < d < n:
            return d
        if d == n:
            return False
        k = k+1

# Defining main function
def main():
    ini_time = time.time()
    print(pollard_P_1(2534389177))
    #print(pollard_P_1(63897587222538985880186825791))
    fin_time = time.time()
    print("Hemos tardado:" + str(float(fin_time-ini_time)) + " SEGUNDOS")

if __name__ == "__main__":
    main()