import collections


def bfs(graph, key):
    visited, queue = set(), collections.deque([key])
    visited.add(key)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [2, 3], 1: [3], 2: [4], 3: [2, 3]}
    print("Breadth First Traversal: ")
    bfs(graph, 0)
