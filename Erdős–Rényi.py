import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def G(N,k):
    mat = np.zeros((N,N)) 
    for i in range(N):
        for j in range(i+1,N):
            if np.random.random() <= k/(N-1):
                mat[i][j]=1 ; mat[j][i]=1 #Symmetric
    return mat

am = G(100,3)    #Adjacency matrix
Gr = nx.DiGraph()
Gr = nx.from_numpy_matrix(am)

G=nx.grid_2d_graph(2,2)  #2x2 grid

pos=nx.spring_layout(G,iterations=100)

plt.subplot(121)
nx.draw_kamada_kawai(Gr, with_labels=False, node_size = 10, width=.3)
plt.title('draw_kamada_kawai')

plt.subplot(122)
nx.draw(Gr, with_labels=False, node_size = 10, width=.3)
plt.title('draw')

plt.show()