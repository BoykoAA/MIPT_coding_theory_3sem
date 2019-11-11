import numpy as np
from sympy import Symbol
from sympy import div

#####################
####input test 2#####
#####################
q = 2
n = 7
coef = 1101
#####################
#####################
#####################

x = Symbol('x')

def Poly(p,mod):
    q,r = div(p,mod,x) #quotient and remainder polynomial division by modulus mod

    return r.as_poly(x,domain='GF(2)') #Z_2

# m = x**8 + x**4 + x**3 + x + 1
# p = x**6 + x**5 + x + 1

m = x**7 + 1
p = x**3 + x + 1

print(Poly(p*p, m))

q: 3
n: 8
polynomial coefficients: 221