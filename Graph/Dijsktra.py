from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)
    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                # 더 가까운 경로를 선택하는 로직
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            # 자기 위치 + edge 길이 (거리)
            weight = currentWeight + graph.distances[(minNode, edge)]
            # 방문한 적 없는 경우
            # 거리가 edge 보다 더 가까운 경우
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(weight)

    return (visited, path)


# 1. 출발 노드를 설정한다.
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다.
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
# 5. 위 과정에서 3번 ~ 4번을 반복한다.

customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

visited, path = dijkstra(customGraph, "A")
print('visited', visited)
print('path', path)
