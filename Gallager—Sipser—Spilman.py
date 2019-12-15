import numpy as np
import sys

####INPUT STEPIK#####

c = 0
for number, line in enumerate(sys.stdin):
    if number == 0:
        codeword = line.split(' ')[-1].split('\n')[0]
    if number == 1:
        continue
        # type_mat = line
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

codeword = np.array(list(map(int, codeword)))
delta = np.sum(matrix) / len(codeword)


def iscodeword(matrix_, codeword_):
    n = np.sum(matrix_.dot(codeword_) % 2)

    return n == 0


while not iscodeword(matrix, codeword):
    idx = np.where(matrix.dot(codeword) % 2 > 0)[1]
    submat = np.array(matrix[idx, :])
    occ = np.sum(submat, axis=0).flatten()
    to_revert = np.argmax(occ)
    ind_occ = np.where(occ > (delta / 2))[0]
    ind_occ = [to_revert]
    if len(ind_occ) == 0:
        break
    else:
        to_revert = ind_occ[0]
        codeword[to_revert] = 1 - codeword[to_revert]

print(''.join(map(str, codeword)))