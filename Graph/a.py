# gdict = graph dictionary
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def __str__(self):
        print(self.gdict)
        return ""

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


# customDict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "g"],
#     "c": ["a", "d", "e"],
#     "d": ["b", "c", "f"],
#     "e": ["c", "f"],
#     "f": ["g", "d", "e"],
#     "g": ["b", "f"]
# }

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "g"],
    "c": ["a", "d", "e"],
    "d": ["b", "c", "f"],
    "e": ["c", "f"],
    "f": ["d", "e", "g"],
    "g": ["b", "f"]
}


graph = Graph(customDict)
graph.dfs("a")
