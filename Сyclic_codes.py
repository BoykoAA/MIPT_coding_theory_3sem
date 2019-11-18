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

def division(m, p, q):
    if q == 2:
        e, r = div(m, p, x)
        pol = r.as_poly(x, domain='GF(2)').args[0]
    else:
        e, r = div(m, p, x)
        pol = r.as_poly(x, domain='GF(3)').args[0]

    return e, r, pol

x = Symbol('x')
m = x**n - 1
p = get_p(coef)

e, r, pol  = division(m, p, q)

if pol == 0:








