import main as graph

def check(adjacency_matrix):
    global fail_count
    mu, phi = graph.eigen(adjacency_matrix)
    n = len(mu)
    max_index = 0

    for i in range(0,n):
        if mu[i] > mu[max_index]:
            max_index = i

    mu_1 = mu[max_index]
    phi_1 = phi[:, max_index]
    phi_1 = list(map(lambda x: abs(x), phi_1))

    max_phi_1_index = 0
    for i in range(0,n):
        if phi_1[i] > phi_1[max_phi_1_index]:
            max_phi_1_index = i

    d_v = graph.find_degree(adjacency_matrix, max_phi_1_index)
    delta = graph.find_max_degree(adjacency_matrix)

    if (abs(delta - d_v) > 0):
        fail_count = fail_count + 1
        # print(adjacency_matrix)
        # print(max_phi_1_index)
        # print(d_v)
        # print(delta)
        # graph.show_graph(adjacency_matrix)
        # exit()


fail_count = 0
n = 50
trials = 10000

for j in range(0,trials):
    g = graph.random_graph(n)
    if graph.is_connected(g):
        check(g)

print(fail_count/trials)
