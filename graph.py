class Graph:
    def __init__(self, edges=[], directed=False):
        self.graph = {}

        for u, v, weight in edges:
            self.insert_edge(u, v, weight)

            if not directed:
                self.insert_edge(v, u, weight)

    def __str__(self):
        string = "{\n"

        for node in self.graph:
            string += f"\t{node}: {self.graph[node]}\n"

        string += "}"
        return string

    def insert_node(self, node):
        self.graph[node] = {}

    def insert_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = {}

        self.graph[start][end] = weight

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]

            for n in self.graph:
                if node in self.graph[n]:
                    del self.graph[n][node]

    def is_connected(self, node1, node2):
        return node1 in self.graph and node2 in self.graph[node1]


def main():
    edges = [(0, 1, 1), (0, 2, 5), (1, 4, 3), (0, 3, 2), (3, 5, 7)]
    graph = Graph(edges)
    print("Graph:", graph)
    print("is_connected(0, 1):", graph.is_connected(0, 1))
    print("is_connected(0, 4):", graph.is_connected(0, 4))

    graph.remove_node(1)
    print("remove_node(1):", graph)


if __name__ == "__main__":
    main()
