import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from numpy import linalg as LA

# Number of vertices
n = int(input())

# Generate a random adjacency matrix
adj = np.zeros((n,n))

for i in range(0,n):
 for j in range(i+1,n):
  r = np.random.uniform(0,1)
  adj[i][j] = round(r)
  adj[j][i] = adj[i][j]

print("Adjacency matrix : ")
print(adj)
print()

# Find eigenvalues/vectors for the adj matrix
w,v = LA.eig(adj)
print("Eigenvalue : Eigenvector")
for i in range(0,len(w)):
 print(w[i], ":", v[:,i])
 print()

# Draw graph
def show_graph_with_labels(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=250, with_labels=True)
    plt.show()

show_graph_with_labels(adj)
