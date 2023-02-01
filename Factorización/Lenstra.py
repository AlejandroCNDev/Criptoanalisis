
import math
import random

from numpy import long


def máximo_común_divisor(a, b):
   '''
   Función que regresa el máximo común divisor entre a y b.
   ''' 

   if abs(b) > abs(a):
      return máximo_común_divisor(b, a)

   while abs(b) > 0:
      _,r = divmod(a,b)
      a,b = b,r

   return a

def inverso_modular(a, b):

# Algoritmo extendido de euclides para obtener el inverso modular de (a modulo b).

   if abs(a) < abs(b):
      (x, y, d) = inverso_modular(b, a)
      return (y, x, d)

   if abs(b) == 0:
      return (1, 0, a)

   x1, x2, y1, y2 = 0, 1, 1, 0
   while abs(b) > 0:
      div, res  = divmod(a,b)
      x = x2 - div*x1
      y = y2 - div*y1
      a, b, x2, x1, y2, y1 = b, res , x1, x, y1, y

   return (x2, y2, a)


class Punto(object):
    def __init__(self, curva, x, y):
        self.x = x
        self.y = y
        self.curva = curva

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Punto(self.curva, self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def suma(self, Q):
        if isinstance(Q, O):
            return self, 1

        x_1 = self.x
        y_1 = self.y

        x_2 = Q.x
        y_2 = Q.y

        mod = self.curva.N

        x_1 %= mod
        y_1 %= mod
        x_2 %= mod
        y_2 %= mod
        
        if x_1 != x_2:
            #Pendiente: (y_1 - y_2)/(x_1 - x_2) -> Euclides extendendido
            u, v, d = inverso_modular(x_1 - x_2, mod)
            s = ((y_1 - y_2) * u) % mod
            x_3 = (s * s - x_1 - x_2) % mod
            y_3 = (-y_1 - s*(x_3 - x_1)) % mod
        else:
            #Si x_1 == x_2 pueden pasar dos cosas:
            #uno: y_1  coincide con -y_2 módulo n
            if (y_1 + y_2) % mod == 0:
                return O(self.curva), 1

            #dos: R = P + P = 2P
            else:
                u, v, d = inverso_modular(2 * y_1, mod)
                s = ((3 * x_1 * x_1 + self.curva.a) * u) % mod
                x_3 = (s * s - 2*x_1) % mod
                y_3 = (-y_1 - s*(x_3 - x_1)) % mod

        return Punto(self.curva, x_3, y_3), d


    def __res__(self, Q):
        return self + (-Q)

    def __mul__(self, n):
        if not (isinstance(n, int) or isinstance(n, long)):
            print(n.__class__.__name__)
            raise Exception("Error: No podemos operar por el tipo.")

        R = O(self.curva)
        d = 1
        while n != 0:
            if n % 2 != 0:
                R, d = self.suma(R)
            if d != 1:
                #Si d != 1, significa que tenemos un factor.
                return R, d 
            self, d = self.suma(self)
            if d != 1:
                return R, d
            n //= 2
        return R, d
 
    def __rmul__(self, n):
        return self * n

def factor(N, bsmooth, iter=5):
    for i in range(iter):
        E, P = curva_random(N);
        Q, d = bsmooth * P
        if d != 1 : return d
    return N

#Punto al infinito.
class O(Punto):
    def __init__(self, curva):
        self.curva = curva

    def __neg__(self):
        return self

    def suma(self, Q):
        return Q, 1

    def __res__(self, Q):
        return -Q

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("No podemos operar por el tipo del valor.")
        else:
            return self, 1

    def __repr__(self):
        return "Infinito."

class CurvaEliptica(object):
    # Curva eliptica: y^2 = x^3 + ax + b
    def __init__(self, a, b, N):
        self.a = a
        self.b = b
        self.N = N

        self.det = 4*(a*a*a) + 27*b*b
        if not self.is_nonsingular():
            raise ValueError("%s es no singular, es decir, el discriminante es 0." % self)

    def is_nonsingular(self):
        return self.det != 0

    def contains(self, x, y):
        return y*y == x**3 + self.a * x + self.b

    def __str__(self):
        return 'y^2 = x^3 + %sx + %s' % (self.a, self.b)


    def __eq__(self,other):
        return (self.a, self.b) == (other.a, other.b)


def curva_random(N):
   '''
   Función que genera una curva aleatoria modulo n.
   '''
   a, x, y = random.randint(1, N), random.randint(1, N), random.randint(1, N)
   b = (y * y - x * x * x - a * x) % N

   E = CurvaEliptica(a, b, N)
   P = Punto(E, x, y)

   return E, P

if __name__=="__main__":
   '''
   Criptología y seguridad de los datos.
   Algoritmo de Lenstra.
   Autor:
      - Alejandro Castro Navarro
   '''

   N = int(input("Introduce N:\n"))

   # Un número es Bsmooth si los factores primos de N son casi B. Aquí escogemos un número muy grande para
   # no tener problemas.
   bsmooth = int(math.factorial(2500))
   counter = 0
   while N != 1:
         k = factor(N, bsmooth)
         k = abs(k)
         if k != 1 and k != N:
            counter = 0
            print("Se encontró un factor: ",end='')
            print(k)
         elif k == 1:
            counter += 1
         N //= k
         if counter >= 30:
            print("Se encontró un factor: ",end='')
            print(N)
            break
