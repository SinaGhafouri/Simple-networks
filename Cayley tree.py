import numpy as np
import random as rn
import networkx as nx
import matplotlib.pyplot as plt
from time import time

def tree(k,p , cayley=True):

    if k != 2 : n = int(1 + k*(((k-1)**p-1)/(k-2)))
    elif k == 2: n = int(1 + 2*p)
    mat = np.zeros((n,n))

    i = np.arange(n) #in
    o = [] #out
    o0 = rn.choice(i) ; o.append(o0) #center
    i = np.delete(i,np.where(i==o[0])[0])
    for _ in range(k):
        new_i = rn.choice(i.tolist())
        mat[new_i][o[0]]=1
        i = np.delete(i,[np.where(i==new_i)[0]])
        o.append(new_i)
    del o[0]
    
    while True:
        if cayley == True: new_o = o[0]
        elif cayley == False: new_o = rn.choice(o)
        for _ in range(k-1):
            new_i = rn.choice(i.tolist())
            mat[new_i][new_o]=1
            i = np.delete(i,[np.where(i==new_i)[0]])
            o.append(new_i)
        del o[o.index(new_o)]

        if len(i)==0: break
    return mat

t1 = time()
mat = tree(k=3,p=4 , cayley = True) #If caylay = False, it will be just a random tree which I don't know what it's called ¯\_(ツ)_/¯
G = nx.from_numpy_matrix(mat)
nx.draw_kamada_kawai(G, with_labels=False, node_size=10,width=.3)
t2 = time()
print('Duration: {:.4} sec'.format(t2-t1))

plt.show()