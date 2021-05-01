from collections import defaultdict


# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict

#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)

#     def bfs(self, vertex):
#         visited = [vertex]
#         queue = [vertex]

#         while queue:
#             deVertex = queue.pop(0)
#             print('BFS', deVertex)
#             for adjacentVertex in self.gdict[deVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     queue.append(adjacentVertex)

#     def dfs(self, vertex):
#         visited = [vertex]
#         stack = [vertex]

#         while stack:
#             popVertex = stack.pop()
#             print("DFS", popVertex)
#             for adjacentVertex in self.gdict[popVertex]:
#                 if adjacentVertex not in visited:
#                     visited.append(adjacentVertex)
#                     stack.append(adjacentVertex)


# customDict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "g"],
#     "c": ["a", "d", "e"],
#     "d": ["b", "c", "f"],
#     "e": ["c", "f"],
#     "f": ["d", "e", "g"],
#     "g": ["b", "f"]
# }

# graph = Graph(customDict)
# graph.bfs('a')
# print("----------------------------------------------------------")
# graph.dfs('a')

# 1. 상위에 있는 걸 먼저 넣어준다.
# 2. 같은 레벨에 있는 걸 먼저 넣어준다.
# 3. 다른 레벨에 있는 걸 먼저 넣어준다.


class Graph2:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def __str__(self):
        print(self.graph)
        return

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for related_vertex in self.graph[vertex]:
            if related_vertex not in visited:
                self.topologicalSortUtil(related_vertex, visited, stack)

        stack.insert(0, vertex)

    def topologicalSort(self):

        visited = []
        stack = []

        for key_vertex in list(self.graph):
            if key_vertex not in visited:
                self.topologicalSortUtil(key_vertex, visited, stack)

        print("visited", visited)
        print("stack", stack)


customGraph = Graph2(9)
customGraph.addEdge('A', 'B')
customGraph.addEdge('A', 'D')
customGraph.addEdge('B', 'C')
customGraph.addEdge('B', 'F')
customGraph.addEdge('C', 'G')
customGraph.addEdge('D', 'E')
customGraph.addEdge('D', 'F')
customGraph.addEdge('E', 'G')
customGraph.addEdge('F', 'G')

customGraph.topologicalSort()
