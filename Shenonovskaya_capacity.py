import numpy as np
from scipy.optimize import linprog
import networkx as nx

general_sample = list(map(int, input().split(' ')))

sample_input = []
for i in range(general_sample[1]):
    sample_input.append(list(map(int, input().split(' '))))

sample_input = [tuple(x) for x in sample_input]

G = nx.Graph()
for i in range(general_sample[0]):
    G.add_node(i + 1)

for j in sample_input:
    G.add_edge(*j)


cliques = list(nx.enumerate_all_cliques(G))


def vectorize(cliques):
    n_cliq = len(list(set([item for sublist in cliques for item in sublist])))
    A_eq = np.ones((1, n_cliq))
    A_eq = np.append(A_eq, 0)

    b_eq = 1

    A_ub = []
    for i in cliques:
        elem_A_ub = np.zeros(n_cliq + 1)

        if len(i) > 1:
            for j in i:
                elem_A_ub[j - 1] = 1
            elem_A_ub[len(elem_A_ub) - 1] = -1
            if len(A_ub) == 0:
                A_ub = elem_A_ub

            else:
                A_ub = np.vstack((A_ub, elem_A_ub))




        else:
            #         elem_A_ub = np.insert(elem_A_ub, i[0]-1, 1)
            #         elem_A_ub = np.insert(elem_A_ub, len(elem_A_ub), -1)
            elem_A_ub[i[0] - 1] = 1
            elem_A_ub[len(elem_A_ub) - 1] = -1

            if len(A_ub) == 0:
                A_ub = elem_A_ub
            else:
                A_ub = np.vstack((A_ub, elem_A_ub))

    b_ub = np.zeros((1, A_ub.shape[0]))

    c = np.zeros((1, n_cliq))
    c = np.insert(c, n_cliq, 1)

    return np.array([A_eq]), np.array([b_eq]), A_ub, b_ub, c


A_eq, b_eq, A_ub, b_ub, c = vectorize(cliques)


res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub,
bounds=(0, None))

res = (res.fun)**(-1)

print(res)