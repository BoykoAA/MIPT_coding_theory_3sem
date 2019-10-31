import numpy as np
import sympy
import sys
from itertools import product, combinations


#Input for stepik
###INPUT
c = 0
for number, line in enumerate(sys.stdin):
    if number == 0:
        q = int(line.split(' ')[1])
    if number == 1:
        type_mat = line
    if number > 1:
        if c == 0:
            line = line.split('\n')[0]
            matrix = list(map(int, line))
            matrix = np.mat(matrix)
            c += 1
        else:
            line = line.split('\n')[0]
            line_mat = list(map(int, line))
            matrix = np.vstack((matrix, line_mat))

matrix = np.mat(matrix, dtype=np.int64)


def gjel(A, p):
    cols_list = []
    col = -1
    """Gauss-Jordan elimination."""
    for i, row1 in enumerate(A):
        pivot_val = 0
        while pivot_val == 0 and col < (A.shape[1] -1):
            col += 1
            pivot = A[i:, col].argmax() + i
            pivot_val = A[pivot, col]
        if pivot_val == 0:
            break
        cols_list.append(col)
        new_row = (A[pivot] * pivot_val) % p  #####
        A[pivot] = A[i]
        row1[:] = new_row

        for j, row2 in enumerate(A):
            if j == i:
                continue
            row2[:] = (row2[:] - new_row * A[j, col]) % p  ####
    return A, cols_list

# generator --> checker
# cheker --> generator
def transforms(matrix, field):
    k, n = matrix.shape
    matrix, col_list = gjel(matrix, p=field)
    result = np.zeros((n-k, n))
    minus_p_col_list = col_list
    eye_list = sorted(list(set(range(n))-set(col_list)))
    result[:, minus_p_col_list] = (-matrix[:, eye_list].T) % field
    result[:, eye_list] = np.diag([1] * (n - k))
    return result

###########################################
# INPUT test_1
#matrix = np.mat([ [0,0,0,1,1,1,1],
#           [0,1,1,0,0,1,1],
#           [1,0,1,0,1,0,1]])
#type_mat = 'parity 1'
#q = int(2)
###########################################


def is_i_suitable(A, i):
   # tuples_list = product(range(A.shape[1]), repeat = i)
   # tuples_list = filter(lambda x: len(set(x))==i, tuples_list)
    # tuples_list = combinations(range(A.shape[1]), i)
    for x in combinations(range(A.shape[1]), i):
        if len(gjel(np.copy(A[:, x]), q)[1]) < i:
            return True
    return False

def find_dist(A):
    for i in range(1, A.shape[0]+1):
        if is_i_suitable(A, i):
            return i
    return A.shape[0] + 1


if type_mat.split(' ')[0] == 'parity':
    H = matrix
    G = transforms(matrix=matrix, field=q)
    d = find_dist(H)
    print('distance: ' + str(d))
    print('generator matrix:')
    for strng in range(G.shape[0]):
        print(''.join(map(str, map(int, np.array(G[strng]).flatten()))))

if type_mat.split(' ')[0] == 'generator':
    G = matrix
    H = transforms(matrix=matrix, field=q)
    d = find_dist(H)
    print('distance: ' + str(d))
    print('parity check matrix:')
    for strng in range(H.shape[0]):
        print(''.join(map(str, map(int, np.array(H[strng]).flatten()))))
