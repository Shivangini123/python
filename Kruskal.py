class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = []

    def add_edge(self, node1, node2, weight):
        self.m_graph.append([node1, node2, weight])

    def find_subtree(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_subtree(parent, parent[i])


    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1

    def kruskals_mst(self):

        result = []


        i = 0

        e = 0


        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])


        parent = []
        subtree_sizes = []


        for node in range(self.m_num_of_nodes):
            parent.append(node)
            subtree_sizes.append(0)


        while e < (self.m_num_of_nodes - 1):

            node1, node2, weight = self.m_graph[i]
            i = i + 1

            x = self.find_subtree(parent, node1)
            y = self.find_subtree(parent, node2)

            if x != y:
                e = e + 1
                result.append([node1, node2, weight])
                self.connect_subtrees(parent, subtree_sizes, x, y)


        for node1, node2, weight in result:
            print("%d - %d: %d" % (node1, node2, weight))

if __name__=="__main__":
    g=Graph(9);

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 7)
    g.add_edge(1, 2, 11)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 5, 20)
    g.add_edge(2, 5, 1)
    g.add_edge(3, 6, 6)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 6, 10)
    g.add_edge(4, 8, 15)
    g.add_edge(4, 7, 5)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 7, 3)
    g.add_edge(6, 8, 5)
    g.add_edge(7, 8, 12)

    g.kruskals_mst();
