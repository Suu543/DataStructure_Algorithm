# Dijkstra's Algorithm for SSSP

![img](https://cdn-images-1.medium.com/max/1000/1*2FzWOFuCBfJLLOyqJeiMrQ.png)

`SingleSourceShortestPath`를 공부하면서, `DFS`를 이용해  `Unweighted Graph`에서는 최단거리를 찾을 수 있지만, `Weighted Graph`에서는 그렇지 않다고 했다.

`Weighted Graph`에서 최단거리를 계산할 때  `Dijkstra's Algorithm`을 사용할 수 있다.

![img](https://cdn-images-1.medium.com/max/1000/1*Vy_L_PrO4PWbzd01IQFPpQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*k51da6oJKky8SRx_RYOJFg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*VVA-iiLT-dD9UdGS5FjF2w.png)

![img](https://cdn-images-1.medium.com/max/1000/1*sVP8oy-qa6ux_rYAx4ihNg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*cCfRs0AHl0F65d-JX2j3zw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*obAWU9kg2KrINhcFRrihfw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*evAFSzId6akrTeS4XBuKWQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ps4fZZeT4Gn0D4NutkzbvA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*5qZsD4YWCTjXPlRCHu9Jpg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*5ENvG-em_Vy2NeBzDimnxA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ayvwy4NqGwB4vy_6tACNbQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*544TDIFTx-qNVFUybwgWkQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*QeoTK12iY2imvfNn6gMang.png)

![img](https://cdn-images-1.medium.com/max/1000/1*lFC2TI83IiQ4ogr0KHmOsg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*kNign_oHw2d5lHeQ-99Q_A.png)

![img](https://cdn-images-1.medium.com/max/1000/1*7--2vwhr7NuCA7Uzj7om_A.png)

1. 출발 노드를 설정한다.
2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장한다.
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택한다.
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신한다.
5. 위 과정에서 3번 ~ 4번을 반복한다.

```python
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
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        print(graph.edges)
        for edge in graph.edges[minNode]:
            print(graph.distances[(minNode, edge)])
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(weight)

    return visited, path


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

print(dijkstra(customGraph, "A"))
```

# Details

```python
dijkstra(customGraph, "A")
visited = { "A": 0 }

nodes = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

distances = {
    ('A', 'B'): 2, 
    ('A', 'C'): 5, 
    ('B', 'C'): 6, 
    ('B', 'D'): 1, 
    ('B', 'E'): 3, 
    ('C', 'F'): 8, 
    ('D', 'E'): 4, 
    ('E', 'G'): 9, 
    ('F', 'G'): 7
}

edges = {
    'A': ['B', 'C'], 
    'B': ['C', 'D', 'E'], 
    'C': ['F'], 
    'D': ['E'], 
    'E': ['G'], 
    'F': ['G']
}

path = {}

while nodes:

# A
minNode = None
if 'A' in visited = True # 출발 노드 설정
minNode = 'A'
nodes.remove('A') # nodes {'B', 'C', 'D', 'E', 'F', 'G'}
currentWeight = 0 # visited['A'] - 출발 노드의 비용을 계산

# 출발 노드를 기준으로 방문할 수 있는 모든 노드의 비용을 계산하고, 최소 비용을 저장
for edge in graph.edges['A'] # ['B', 'C'] 
# A를 기준으로 B까지의 거리를 계산
weight = currentWeight(0) + graph.distances[(minNode('A'), edge('B'))](2) = 2
# 방문한 적이 없는 경우 - visited에 등록 A ~ 방문한 적 없는 곳까지의 거리
'B' not in visited = True
visited['B'] = weight(2) # visited = { "A": 0, "B": 2 }
path['B'].append(weight(2)) # path = { 'B': 2 }

weight = currentWeight(0) + graph.distance[(minNode('A'), edge('C'))](5) = 5
# 방문한 적이 없는 경우 - visited에 등록 A ~ 방문한 적 없는 곳까지의 거리
'C' not in visited = True
visited['C'] = weight(5) # visited = { "A": 0, "B": 2, "C": 5 }
path['C'].append(weight(5)) # path = { 'B': 2, 'C': 5 }

# ---------------------------------------------------------------------------------------
# nodes에서 'A'는 제거된 상태
# Nodes {'B', 'C', 'D', 'E', 'F', 'G'}
# visited = { "A": 0, "B": 2, "C": 5 }
'B' in nodes = True 
minNode = None
if 'B' in visited = True
minNode = 'B' # 출발 노드 설정

if 'C' in visited = True
if minNode is None = False
if visited['C'] (5) < visited['B'] (2) = False
minNode = 'B' # B가 C보다 더 거리가 짧기 때문에, B를 기준으로 경로 탐색
nodes.remove('B') # nodes {'C', 'D', 'E', 'F', 'G'}
currentWeight = 2 # visited["B"]

# B를 기준으로 방문할 수 있는 모든 노드의 비용을 계산하고, 최소 비용을 저장
for edge in graph.edges['B'] # ['C', 'D', 'E']
weight = currentWeight(2) + graph.distance[(minNode('B'), edge('C'))](6) = 8
# 방문한 적이 있기 때문에 기록으로 남기지 않아도 된다.
'C' not in visited = False
# B를 거쳐 C로 가는 것이, A(시작점) C까지의 거리 보다 더 멀기 때문에 고려 대상이 아니다.
weight(6) < visited['C'](5) = False 
# visited = { "A": 0, "B": 2, "C": 5 }
# path = { 'B': 2, 'C': 5 }

weight = currentWeight(2) + graph.distance[(minNode('B'), edge('D'))](1) = 3
# 방문한 적이 없기 때문에 기록으로 남겨야 한다.
'D' not in visited = True
# currentWeight(A ==> B) + (B ==> D) ==> D = 3 (3은 A ~ D 까지의 거리를 의미한다)
visited['D'] = weight(3) # visited = { "A": 0, "B": 2, "C": 5, "D": 3 }
path['D'].append(weight(3)) # path = { 'B': 2, 'C': 5, "D": 3 }

weight = currentWeight(2) + graph.distance[(minNode('B'), edge('E'))](3) = 5
# 방문한 적이 없기 때문에 기록으로 남겨야 한다.
'E' not in visited = True
# currentWeight(A ==> B) + (B ==> E) ==> E = 5 (3은 A ~ D 까지의 거리를 의미한다)
visited['E'] = weight(5) # visited = { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5 }
path['E'].append(weight(5)) # path = { "B": 2, "C": 5, "D": 5, "E": 5}

# ---------------------------------------------------------------------------------------
# nodes에서 'A', 'B'는 제거된 상태
# Nodes { 'C', 'D', 'E', 'F', 'G' }
# visited = { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5}
'C' in nodes = True
minNode = None
if 'C' in visited = True
minNode = 'C' # 출발 노드 설정

'D' in nodes = True
minNode = 'C'
minNode is None = False
visited['D'](3) < visited['C'](5) = True
# 출발 노드 설정 (D가 C보다 더 최적 경로이기 때문에)
minNode = 'D' 

'E' in nodes = True
minNode = 'D'
minNode is None = False
visited['E'](5) < visited['D'](3) = False
# 출발 노드 설정 (D가 E보다 더 최적 경로이기 때문에)
minNode = 'D'

nodes.remove('D') # nodes { 'C', 'E', 'F', 'G' }
currentWeight = 3 # visited['D']
# D를 기준으로 방문할 수 있는 모든 노드의 비용을 계산하고, 최소 비용을 저장
for edge in graph.edges['D'] # ['E']
weight = currentWeight(3) + graph.distance[(minNode('D'), edge('E'))](4) = 7
# 방문한 적이 있기 때문에 기록으로 남기지 않아도 된다.
'E' not in visited = False
# D를 거쳐 E로 가는 것보다, B --> E로 가는 것이 최적 경로이기 때문에 고려 대상이 아니다.
weight(7) < visited['E'](5) = False

# ---------------------------------------------------------------------------------------
# nodes에서 'A', 'B', 'D'는 제거된 상태
# Nodes { 'C', 'E', 'F', 'G' }
# visited = { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5}

'C' in nodes = True
minNode = None
if 'C' in visited = True
minNode = 'C' # 출발 노드 설정

'E' in nodes = True
minNode is None = False
visited['E'](5) < visited['C'](5) = False
# 출발 노드 설정 (E가 C보다 더 최적 경로가 아니기 때문에)
minNode = 'C'

nodes.remove('C') # nodes { 'E', 'F', 'G' }
currentWeight = 5 # visited['C']
for edge in graph.edges['C'] # ['F']
# C를 기준으로 방문할 수 있는 모든 노드의 비용을 계산하고, 최소 비용을 저장
weight = currentWeight(5) + graph.distance[(minNode('C'), edge('F'))](8) = 13
# 방문한 적이 없기 때문에 기록으로 남겨야 한다.
'F' not in visited = True
# (A ==> C) + (C ==> F) = 13 
visited['F'] = weight(13)
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13 }
path['F'].append(weight(13)) 
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13 }

# ---------------------------------------------------------------------------------------
# nodes에서 'A', 'B', 'D', 'C'는 제거된 상태
# Nodes { 'E', 'F', 'G' }
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13 }
'E' in nodes = True
minNode = None
if 'E' in visited = True
minNode = 'E' # 출발 노드 설정

'F' in nodes = True
minNode is None = False
visited['F'](13) < visited['E'](5) = False
minNode = 'E'
# 출발 노드 설정 (F가 E보다 더 최적 경로가 아니기 때문에)

nodes.remove('E') # nodes { 'F', 'G' }
currentWeight = 5 # visited['E']
for edge in graph.edges['E'] # ['G']
# E를 기준으로 방문할 수 있는 모든 노드의 비용을 계산하고, 최소 비용을 저장
weight = currentWeight(5) + graph.distance[(minNode('E'), edge('G'))](9) = 14
# 방문한 적이 없기 때문에 기록으로 남겨야 한다.
'G' not in visited = True
# (A ==> B) + (B ==> E) + (E ==> G) = 14
visited['G'] = weight(14)
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13, "G": 14 }
path['G'].append(weight(14))
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13, "G": 14 }
# ---------------------------------------------------------------------------------------
# nodes에서 'A', 'B', 'D', 'C', 'E' 는 제거된 상태
# Nodes { 'F', 'G' }
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13, "G": 14 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13, "G": 14 }
'F' in nodes = True
minNode = None
if 'F' in visited = True
minNode = F # 출발 노드 설정

'G' in nodes = True
minNode is None = False
visited['G'](14) < visited['F'](13) = False
minNode = F
# 출발 노드 설정 (G가 E보다 더 최적 경로가 아니기 때문에)

nodes.remove('F') # nodes { 'G' }
currentWeight = 13 # visited['F']
for edge in graph.edges['F'] # ['G']
weight = currentWeight(13) + graph.distance[(minNode('F'), edge('G'))](7) = 20
'G' not in visited = False
# F를 거쳐 G로 가는 것보다, G 까지의 최적 경로 값이 더 작기 때문에 고려 대상이 아니다.
weight(20) < visited['G'](14) = False
# ---------------------------------------------------------------------------------------
# nodes에서 'A', 'B', 'D', 'C', 'E' 는 제거된 상태
# Nodes { 'G' }
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13, "G": 14 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13, "G": 14 }

'G' in nodes = True
minNode = None
if 'G' in visited = True
minNode = 'G' # 출발 노드 설정

nodes.remove('G') # { }
currentWeight = 14 # visited['G']
# 'G'는 edges가 없기 때문에 순회할 요소가 없다.

#---------------------------------------------------------------------------------------
minNode = None
# nodes에는 더 이상 순회할 요소가 없다.
if minNode is None = True
break

# while 문을 빠져나온다.
# visited { "A": 0, "B": 2, "C": 5, "D": 3, "E": 5, "F": 13, "G": 14 }
# path = { "B": 2, "C": 5, "D": 5, "E": 5, "F": 13, "G": 14 }
return visited, path
```

## Dijkstra's Algorithm with negative cycle

A path is called a negative cycle if:

There is a cycle (a cycle is a path fo edges or vertices wherein a vertex is reachable from itself)

Total weight of cycle is a negative number

![img](https://cdn-images-1.medium.com/max/1000/1*Y-FMR18TACmnbdrnc46SGg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*zkGikYjDOI4s29aiTrLJqQ.png)

`Negative Cycle`이 발생하는 그래프에서는, `최소 경로(The minimum distance)`를 찾을 수 없다.

Path from A to B

= -6 + 1 = -5

= (one more cycle) = -5 + 3 + (-6) + 1 = -7

= (one more cycle) =  -7 + 3 + (-6) + 1 = -9

The more cycles that we take, every time the distances starts decreasing.

Dijkstra algorithm cannot catch the negative cycle. In order to solve this problem, we can user another algorithm which is called Bellman Ford Algorithm, which deals with negative cycle successfully.



























