class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def get_vertices(self):
        return  list(self.graph.keys())

    def get_adges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))
        return edges


graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")

verticles = graph.get_vertices()
print(verticles)

edges = graph.get_adges()
print(edges)


