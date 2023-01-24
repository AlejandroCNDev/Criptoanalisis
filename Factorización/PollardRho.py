
from random import randint
import math

# Require: Un número entero positivo compuesto n
# Ensure: Un factor de n
def pollard_rho(n):
    A = B = randint(2, n - 1)#Habitualmente A = B = 2
    #A = B = 2

    while True:
        A = (pow(A, 2) + 1) % n
        B = (pow(B, 2) + 1) % n
        B = (pow(B, 2) + 1) % n
        p = math.gcd(A - B, n)
        if 1 < p < n:
            return p
        if p == n:
            return n

# Defining main function
def main():
    print(pollard_rho(2534389177))
    print(pollard_rho(18446744073709551617))
    print(pollard_rho(7))
    print(pollard_rho(39617))

if __name__ == "__main__":
    main()