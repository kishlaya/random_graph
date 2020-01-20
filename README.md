# Random Graph Generator

- Generates a random graph
- Consider the adjacency matrix of this graph
- Find all its eigenvalues and corresponding eigenvectors
- Draw the graph


## Conjecture 1

Let G be a connected graph. Consider the eigenvector x of the largest eigenvalue.
Then x(u) \geq x(v) iff degree(u) \geq degree(v)

This turned out to be **FALSE** (See conj1.py)


## Conjecture 2

Let G be a connected graph. Consider the eigenvector x of the largest eigenvalue.
Let u be the vertex such that x(u) is largest. Then u is the vertex of maximum degree.

This turned out to be **FALSE** (See conj2.py)
