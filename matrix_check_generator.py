from collections import OrderedDict
import numpy as np
import math
import sympy

n,d,q = map(int, input().split(' '))

def hammig(n,d,q):
    t= math.floor((d-1)/2)

    denominator = 0
    for k in range(0, t+1):
        denominator += sympy.binomial(n, k) * (q - 1)**k

    hemming = q**n // denominator
    return hemming

def singlton(n,d,q):
    singlton = math.floor(q**(n-d+1))
    return singlton

def elias(n,d,q):
    t = math.floor(  ( (1 - np.sqrt(1-(2*d/n))) / 2 ) * n - 1      )
    S_t = 0
    for k in range(0, t+1):
        S_t += sympy.binomial(n, k)
    elias = 2**n * n // S_t
    return elias


def sum_x(M, n, d, q):
    first_number = []
    second_number = []
    
    for i in range(1000000):
        numb = round(M/q)
        if q-i < 0:
            for j in range(1000000):
                sum_x = (numb-1) * (q-j) + (numb*j)

                if sum_x == M:

                    for z in range(q-j):
                        first_number.append(numb-1)
                    for z in range(j):
                        second_number.append(numb)
                    
                    return first_number, second_number
                    break
        else:            
            if i == 0: 
                sum_x =  (numb+1) * q
            elif i >= 1:
                sum_x = (numb+1) * (q-i) + (numb*i)


            if sum_x == M:
                for z in range(q-i):
                    first_number.append(numb+1)
                for z in range(i):
                    second_number.append(numb)
                    
                return first_number, second_number
                break

                
def plotkin(n,d,q):
    diff = 0
    if q*d <= (q-1)*n:
        n2 = q*d / (q-1)
        n2 = math.ceil(n2) - 1
        diff = n - n2

    n -= diff
    M_default = int(math.ceil(d/(d-n*(1-(1/q)))))


    # for M in np.arange(M_default, math.floor(M_default/2), -1):
    for M in np.arange(M_default, 0, -1):
        first_number, second_number = sum_x(M, n, d, q)

        sum_multy_x = 0
        for f in first_number:
            for s in second_number:
                sum_multy_x += f*s

        if len(first_number) == 0:
            sum_multy_x += sympy.binomial(len(second_number), 2) * second_number[0]* second_number[0]

        elif len(second_number) == 0:
            sum_multy_x += sympy.binomial(len(first_number), 2) * first_number[0] * first_number[0]

        elif len(first_number) > 0 and len(second_number) > 0:    
            sum_multy_x += sympy.binomial(len(first_number), 2) * first_number[0] * first_number[0]
            sum_multy_x += sympy.binomial(len(second_number), 2) * second_number[0]* second_number[0]


        right_part = sum_multy_x * n    
        left_part = d * ((M*(M-1))/2)


        if left_part <= right_part:
            M = M * (q**diff)
#             print('success!', 'M =', M)
            return M
            break
    


# 𝑞=2  и 2𝑑<𝑛.    

                
if q == 2 and 2*d < n:
    ham = hammig(n,d,q)
    plot = plotkin(n,d,q)
    sing = singlton(n,d,q)
    el = elias(n,d,q)
    
    res_name = OrderedDict([
        ('hamming', ham),
        ('elias', el),
        ('singleton', sing),
        ('plotkin', plot)
    ])
    
    best = min(res_name, key=res_name.get)
    print('best:', best)
    for name, values in sorted(res_name.items()):
        print(name + ':', values)

else:
    ham = hammig(n,d,q)
    plot = plotkin(n,d,q)
    sing = singlton(n,d,q)
    
    res_name = OrderedDict([
        ('hamming', ham),
        ('singleton', sing),
        ('plotkin', plot)
    ])
    
    best = min(res_name, key=res_name.get)
    print('best:', best)
    for name, values in sorted(res_name.items()):
        print(name + ':', values)
