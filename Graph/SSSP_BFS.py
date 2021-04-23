class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            # 이차원 리스트
            path = queue.pop(0)
            # print(id(path[0]))
            node = path[-1]
            # print(node)
            if node == end:
                # Reach the destination
                return path
            for adjacent in self.gdict.get(node, []):
                # get(node, []) --> A value to return if the specified key does not exist
                # list() --> Double Check Purpose
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customDict = {
    "A": ["B", "C"],
    "B": ["D", "G"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "G": ["F"]
}

graph = Graph(customDict)
print(graph.bfs("A", "F"))
