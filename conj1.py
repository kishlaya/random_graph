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
    test = []
    for i in range(0,n):
        x = abs(phi_1[i])
        y = graph.find_degree(adjacency_matrix, i)
        test.append((i,x,y))

    test.sort(key=lambda x: x[1])
    for i in range(0,n-1):
        d_u = test[i][2]
        d_v = test[i+1][2]
        if d_u > d_v:
            fail_count = fail_count + 1
            break
            # print(adjacency_matrix)
            # print()
            # print(test)
            # print()
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
