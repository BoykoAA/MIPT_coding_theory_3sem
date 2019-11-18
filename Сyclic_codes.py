import numpy as np
from sympy import Symbol
from sympy import div

#####################
####input test 2#####
#####################
q = 2
n = 7
coef = [1,1,0,1]
#####################
#####################
#####################

def get_p(coef):
    p = 0
    for idx_c, c in enumerate(coef):
        if c > 0:
            p += c * x ** idx_c

    return p

def division(m, p):
    q, r = div(m, p, x)
    pol = r.as_poly(x, domain='GF(2').args[0]

    return q, r, pol

x = Symbol('x')
m = x**n - 1
p = get_p(coef)

q, r, pol  = division(m, p)

if pol == 0:
    q

def Poly(p,mod):
    q,r = div(p,mod,x) #quotient and remainder polynomial division by modulus mod

    return r.as_poly(x,domain='GF(2)') #Z_2

# m = x**8 + x**4 + x**3 + x + 1
# p = x**6 + x**5 + x + 1

m = x**7 + 1
p = x**3 + x + 1

print(Poly(p*p, m))
