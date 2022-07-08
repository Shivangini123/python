INF = 1000000000
def floyd_warshall(vertex, adjacency_matrix):
    for s in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
             adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][s] + adjacency_matrix[s][j])

    print("o/d", end='')
    for i in range(0, vertex):
        print("\t{:d}".format(i+1), end='')
    print();
    for i in range(0, vertex):
        print("{:d}".format(i+1), end='')
        for j in range(0,vertex):
            print("\t{:d}".format(adjacency_matrix[i][j]), end='')
        print();
adjacency_matrix = [
                    [  0,   1, 3, INF],
                    [  1,   0, 1, INF],
                    [  3,   1, 0,   2],
                    [INF, INF, 2,   0]
                    ]
floyd_warshall(4, adjacency_matrix);
