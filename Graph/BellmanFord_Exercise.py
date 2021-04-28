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
        return

    def bellmanFordWormhole(self, src):
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
    results = []
    num_of_test = int(input())

    # branch = 지점, road = 도로, wormhole = 웜홀
    for _ in range(num_of_test):
        branch, road, wormhole = map(int, input().split())
        graph = Graph(branch)

        for node in range(1, branch + 1):
            graph.addNode(node)

        for _ in range(road):
            start, end, time = map(int, input().split())
            graph.addEdge(start, end, time)
            graph.addEdge(end, start, time)

        for _ in range(wormhole):
            start, end, time = map(int, input().split())
            graph.addEdge(start, end, -time)

        # 음수 값이 v - 1 번의 최단거리 계산 결과에 영향을 미치는가 확인
        isAffected = graph.bellmanFordWormhole(1)
        if isAffected:
            results.append("Yes")
        else:
            results.append("No")

    for result in results:
        print(result)


run()
