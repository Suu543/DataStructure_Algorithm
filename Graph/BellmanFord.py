#   Created by Elshad Karimov
#   Copyright © 2021 AppMillers. All rights reserved.


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
            print('  ' + key, ' :    ', value)

    def bellmanFord(self, src):
        # dist represents for dictionary
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.vertices-1):
            for source, destination, weight in self.graph:
                print(
                    f"vertices: {_} source: {source} destination: {destination} weight: {weight}")
                # Infinity means it has not been tracked or visited
                # if the current weight is smaller than the previous one, it will be replaced
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

        # Identify the negative cyvle
        for source, destination, weight in self.graph:
            # If any weight is changed after (vertices - 1) times iteration,
            # it means that the graph contains a negative cycle.
            # In order to get the shortest path, we need to stop and return the result
            if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                print("Graph contains negative cycle")
                return

        self.print_solution(dist)


g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")
