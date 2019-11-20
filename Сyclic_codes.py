import numpy as np
from sympy import Symbol
from sympy import div

q = int(input().split(': ')[1])
n = int(input().split(': ')[1])
coef = list(map(int, list(input().split(': ')[1])))


def get_p(coef):
    p = 0
    for idx_c, c in enumerate(coef):
        if c > 0:
            p += c * x ** idx_c

    return p


def division(m, p, q):
    if q == 2:
        e, r = div(m, p, x)
        pol_r = r.as_poly(x, domain='GF(2)').args[0]
        pol_e = e.as_poly(x, domain='GF(2)').args[0]

    else:
        e, r = div(m, p, x)
        pol_r = r.as_poly(x, domain='GF(3)').args[0]
        pol_e = e.as_poly(x, domain='GF(3)').args[0]

    return pol_e, pol_r


def shift(l):
    for i in range(len(l) - 1):
        l[i] = l[i + 1]
    l[len(l) - 1] = 0

    return l


def get_check_poly(check_poly):
    for i in range(len(check_poly) - 1, 0, -1):
        if check_poly[i] == 0 and check_poly[i - 1] == 0:
            continue
        elif check_poly[i] == 0 and check_poly[i - 1] != 0:
            return (check_poly[:i])


check_poly = []
x = Symbol('x')
m = x ** n - 1
p = get_p(coef)

e, r = division(m, p, q)
if r == 0:
    coef_full = coef + [0] * (n - len(coef))
    m = np.zeros((1, n + 1))
    for arg in e.args:
        try:
            number = int(arg)
            m[0][-1] = number
            check_poly.append(number)
        except:
            continue

    for pol in range(1, n + 1):
        m[0][-1 - pol] = e.coeff(x ** pol)
        check_poly.append(e.coeff(x ** pol))

    check_poly = get_check_poly(check_poly)
    check_poly = map(lambda t: t if t >= 0 else q + t, check_poly)

    st = ''
    for chp in check_poly:
        st += str(chp)

    print('parity check polynomial:' + ' ' + str(st))
    print('generator matrix:')


    def cyclic_perm(some_list, some_shift):
        return some_list[len(some_list) - some_shift:] + some_list[:len(some_list) - some_shift]


    for i in range(n - len(coef) + 1):
        print(''.join(map(str, cyclic_perm(coef_full, i))))

else:
    print('not a generator polynomial')