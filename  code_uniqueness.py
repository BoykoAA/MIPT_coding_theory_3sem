#!/usr/bin/env python

from itertools import product
import numpy as np
import networkx as nx
import sys

## step inp
def inp():
    return list(map(lambda x: x.split('\n')[0], sys.stdin.readlines()))[1:]

words = inp()

def prefix_free(words):
    prefixs = []
    for w1, w2 in combinations(words, 2):
        if len(w1) == len(w2):
            if w1 == w2:
                prefixs.append(w1)
        elif len(w1) < len(w2):
            if w1 == w2[:len(w1)]:
                prefixs.append(w1)
        elif len(w2) < len(w1):
            if w2 == w1[:len(w2)]:
                prefixs.append(w2)
            
    return list(set(prefixs))

def suffix_free(words):
    suffixs = []
    for w1, w2 in combinations(words, 2):
        if len(w1) == len(w2):
            if w1 == w2:
                suffixs.append(w1)
        elif len(w1) < len(w2):
            if w1 == w2[-len(w1):]:
                suffixs.append(w1)
        elif len(w2) < len(w1):
            if w2 == w1[-len(w2):]:
                suffixs.append(w2)
    
    return list(set(suffixs))       
        

def get_proper_suff(some_str):
    return [some_str[i:] for i in range(1, len(some_str))]

def get_proper_pref(some_str):
    return [some_str[:-i] for i in range(1, len(some_str))]

A = []
for i in map(get_proper_pref, words):
    A += i
A=set(A)
B = []
for i in map(get_proper_suff, words):
    B += i
    
B=set(B)
is_pref_free_code = (len(set(words)) == len(words) and len(A & set(words)) == 0)
is_suf_free_code = (len(set(words)) == len(words) and len(B & set(words)) == 0)

C = (A & B) - set(words)
C.add('')

def isseq(sword, filter_len):
    if sword == '':
        return []
    good_words = filter(lambda x: len(x)<=len(sword) and len(x)<filter_len and sword[:len(x)]==x, words)
    for x in good_words:
        res = isseq(sword[len(x):], filter_len)
        if res != -1:
            return [x] + res
    return -1

def isseq_all_razbienie(sword):
    result=[]
    if sword == '':
        return [[]]
    good_words = filter(lambda x: len(x)<=len(sword) and sword[:len(x)]==x, words)
    for x in good_words:
        result_tmp = isseq_all_razbienie(sword[len(x):])
        result += map(lambda y: [x] + y, result_tmp)
    return result

G = nx.MultiDiGraph()

for x, y, z in product(C, C, set(words)):
    if len(x) <= len(z):
        if x == z[:len(x)]:
            if len(y) <= len(z):
                if y == z[-len(y):] or y == '':
                    if len(x) + len(y) <= len(z):
                        mid = z[len(x):len(z)-len(y)]
                        
                        t = isseq(mid, len(z))
                        if t != -1:
                            G.add_edge(x, y, weight=len(z)-len(y), path=t)
                            
best_short = 0
best_len = -1
for x in list(G.nodes):
    if x == '':
        continue
    
    try:
        fst_path = nx.dijkstra_path(G, '', x)
        fst_path_length = nx.dijkstra_path_length(G, '', x)
        fst_path_complicated = []
        for u,v in zip(fst_path[:-1], fst_path[1:]):
            all_edges = list(G[u][v].values())
            fst_path_complicated += all_edges[np.argmin(map(lambda x: x['weight'], all_edges))]['path']
            fst_path_complicated += [v]
    except nx.NetworkXNoPath:
        continue

    try:
        all_edges = G[x]['']
    except KeyError:
        continue
    all_edges = list(all_edges.values())
    if len(all_edges) == 0:
        continue
    snd_path_complicated = all_edges[np.argmin(map(lambda x: x['weight'], all_edges))]['path']
    snd_path_length = min(map(lambda x: x['weight'], all_edges))

    path = fst_path_complicated + snd_path_complicated
    path_length = fst_path_length + snd_path_length
    if best_len == -1 or path_length < best_len:
        best_short = path
        best_len = path_length

petli = filter(lambda x: x[0]=='' and x[1]=='', G.edges(data=True))
petli = list(petli)

if (len(petli) > 0):
    best_petlya_weight = np.argmin(map(lambda x: x[2]['weight'], petli))
    best_petlya_path = petli[best_petlya_weight][2]['path'] 
    if best_petlya_weight < best_len or best_len == -1:
        best_short = best_petlya_path
        best_len = petli[best_petlya_weight][2]['weight']

def out(pref, suff, seq):
    print('prefix-free: ' + pref)
    print('suffix-free: ' + suff)
    print('minimal ambiguous sequence: ' + seq)

def print_ans(some_razbienie):
    pref_str="yes" if is_pref_free_code else "no"
    suf_str="yes" if is_suf_free_code else "no"
    out(pref_str, suf_str, some_razbienie)

def get_ans(ambiguous_word):
    all_razbieniya = isseq_all_razbienie(ambiguous_word)
#     print all_razbieniya
    fst_index = 0
    snd_index = 1
    if len(all_razbieniya[0][0])>len(all_razbieniya[1][0]):
        fst_index = 1
        snd_index = 0
    return '-'.join(all_razbieniya[fst_index]) + '=' + '-'.join(all_razbieniya[snd_index])

if best_len == -1:
    print_ans('(none)')
else:
    neodnoznach_slovo = ''.join(best_short)
    print_ans(get_ans(neodnoznach_slovo))

