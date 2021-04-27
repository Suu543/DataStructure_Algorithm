# https://www.acmicpc.net/problem/1865
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []

    def addEdge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def addNode(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('  ' + key, ' :    ', value)

    def bellmanFord(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.vertices - 1):
            for source, destination, weight in self.graph:
                if dist[source] != float('Inf') and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

        for source, destination, weight in self.graph:
            if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                print("Graph contains negative cycle")
                return

        self.print_solution(dist)

    def bellmanFord_Application_Version(self, src):
        dist = {i: float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.vertices - 1):
            for source, destination, weight in self.graph:
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

            # 음수임에도, dist[destionation] (기존에 계산된 최단거리) 보다 작은 값이 나오지 않는다면,
            # 조건을 통과하지 못한다.
            for source, destination, weight in self.graph:
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    return True

        return False


def run():
    num_of_test = int(input())

    for _ in range(num_of_test):
        n, m, w = map(int, input().split())
        g = Graph(n)

        # n = 지점
        for node in range(1, n + 1):
            g.addNode(node)

        # m = 도로
        for _ in range(m):
            s, e, t = map(int, input().split())
            g.addEdge(s, e, t)
            g.addEdge(e, s, t)

        # w = 웜홀
        for _ in range(w):
            s, e, t = map(int, input().split())
            g.addEdge(s, e, -t)

        # 음수 값이 v - 1 번의 최단거리 계산 결과에 영향을 미치는가 확인
        isAffected = g.bellmanFord_Application_Version(1)
        if isAffected:
            print("Yes")
        else:
            print("No")


run()
