import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def snobbish(N,p,q):
    M = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            rand = np.random.random()
            if (i >= N/2 and j < N/2) | (i < N/2 and j >= N/2):
                if rand <= q: M[i][j] = 1 ; M[j][i] = 1
            elif (i >= N/2 and j >= N/2) | (i < N/2 and j < N/2):
                if rand <= p: M[i][j] = 1 ; M[j][i] = 1
    return M

am = snobbish(100,.9,.1)    #Adjacency matrix
Gr = nx.DiGraph()
Gr = nx.from_numpy_matrix(am)
nx.draw_circular(Gr, with_labels=False, node_size = 10, width=.1)

plt.show()