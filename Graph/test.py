class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print(' ' + key, ' : ', value)

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.vertices - 1):
            for source, destination, weight in self.graph:
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

        for source, destination, weight in self.graph:
            if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                print("This Graph contains negative cycle")
                return

        self.print_solution(dist)
