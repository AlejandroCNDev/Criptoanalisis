import math

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

# trying to solve 8576(BETA) = 3(Alpha)^x (mod 53047(primo))

primo = 53047
alpha = 3
beta = 8576
#The correct answer is x = 1234

print(baby_step_giant_step(primo, alpha, beta))

print(((3**1234)%53047))

#EXAMPLE CSD

# trying to solve 124(BETA) = 2(Alpha)^x (mod 383(primo))

primo = 383
alpha = 2
beta = 124
#The correct answer is x = 45

print(baby_step_giant_step(primo, alpha, beta))

print(((2**45)%383))







###############################################

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
            num_32.append([p,alpha,beta,orden])
        elif n == 36:
            num_36.append([p,alpha,beta,orden])
        elif n == 40:
            num_40.append([p,alpha,beta,orden])
        elif n == 44:
            num_44.append([p,alpha,beta,orden])
        elif n == 48:
            num_48.append([p,alpha,beta,orden])
        elif n == 52:
            num_52.append([p,alpha,beta,orden])
        elif n == 56:
            num_56.append([p,alpha,beta,orden])
        elif n == 60:
            num_60.append([p,alpha,beta,orden])
        elif n == 64:
            num_64.append([p,alpha,beta,orden])
        elif n == 80:
            num_80.append([p,alpha,beta,orden])
        elif n == 96:
            num_96.append([p,alpha,beta,orden])
        elif n == 112:
            num_112.append([p,alpha,beta,orden])
        elif n == 128:
            num_128.append([p,alpha,beta,orden])

    except ValueError:
        print(f"Line {line} is not in the expected format")

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



