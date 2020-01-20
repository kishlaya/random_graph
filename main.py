import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from numpy import linalg as LA

# Generate a random adjacency matrix
def random_graph(n):
    adj = np.zeros((n,n))

    for i in range(0,n):
        for j in range(i+1,n):
            r = np.random.uniform(0,1)
            adj[i][j] = round(r)
            adj[j][i] = adj[i][j]

    return adj

# Find eigenvalues/vectors for the adj matrix
def eigen(adjacency_matrix):
    return LA.eig(adjacency_matrix)

# Draw graph
def show_graph(adjacency_matrix):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=250, with_labels=True)
    plt.show()

def find_degree(adjacency_matrix, i):
    return sum(adjacency_matrix[i])

def find_max_degree(adjacency_matrix):
    n = adjacency_matrix.shape[0]
    vertices = list(range(0,n))
    degrees = map(lambda i: find_degree(adjacency_matrix, i), vertices)
    return max(degrees)

def is_connected(adjacency_matrix):
    mu, phi = eigen(adjacency_matrix)
    mu.sort()
    if mu[-2] == mu[-1]:
        return False
    return True
