# Single Source Shortest Path

1. Single Source Shortest Path Problem (SSSPP)
2. BFS for SSSPP
3. BFS for SSSPP in Python
4. Why does BFS not work with weighted Graph?
5. Why does DFS not work for SSSP?

## Single Source Shortest Path Problem

A single source problem is about finding a path between a given vertex (called source) to all other vertices in a graph such that the total distance between them (source and destination) is minimum.

The problem:

- Five offices in different cities.
- Travel costs between these cities are known.
- Find the cheapest way from head office to branches in different cities.

**Expensive Way**

![img](https://cdn-images-1.medium.com/max/1000/1*lPDpap8AUY_GV8OKITCThg.png)

**Cheapest Way**

![img](https://cdn-images-1.medium.com/max/1000/1*xbAq6aF9YYZwoonfBIJYoQ.png)

**There are three algorithms that we can use to solve this single source shortest path problem**

![img](https://cdn-images-1.medium.com/max/1000/1*kt31RyYb3GwzfgxQqmJ6Kg.png)

- BFS
  - BFS Logic에 `Parent` 개념을 더해주면된다. 
    - Vertex `B`의 부모는 `A`
    - Vertex `C`의 부모는 `B` 
    - Vertex `D`의 부모는 `C`
- Dijkstra's Algorithm
- Bellman Ford

## BFS for SSSP

![img](https://cdn-images-1.medium.com/max/1000/1*--J3g4ZE_ZXPt9gNfK7dhA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*G439_hnfBwNIhBiltgiWQg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*G439_hnfBwNIhBiltgiWQg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*DI9kSaat_r5C2p1ZH55Low.png)

![img](https://cdn-images-1.medium.com/max/1000/1*rjivb1Q1oT3HTC9d3M8X6g.png)

![img](https://cdn-images-1.medium.com/max/1000/1*T2c4risPdKll-mjh-Hh8tQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*b6J_KVVIehvdGTThikzvrw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*bzlmCSgHQHTSJl5yLVsNsA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*LpWhTO9NQ4KDWtRQhXMGFA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*OReFhNQ9-7GLYK2w9WsA1w.png)

![img](https://cdn-images-1.medium.com/max/1000/1*jNIc6rFjldRtutSUD7WnRw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*otNgN0gLFMCB4-dioA54xw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*0CyAkqpvX17SyUu6rAT9Tw.png)

```python
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                # Reach the destination
                return path
            for adjacent in self.gdict.get(node, []):
                # get(node, []) --> A value to return if the specified key does not exist
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

#----------------------------------------------------------------------------------------
queue = [
    ["A"]
], 
path = ["A"], node = "A", node != end
adjacent in ["B", "C"] - A
new_path = ["A","B"]
queue = [["A", "B"]]
new_path = ["A", "C"]
queue = [["A", "B"], ["A", "C"]]

queue = [
    ["A", "B"] (POP), 
    ["A", "C"]
], 
path = ["A", "B"], node = "B", node != end
adjacent in ["D", "G"] - B
new_path = ["A", "B", "D"]
queue = [["A", "C"], ["A", "B", "D"]]
new_path = ["A", "B", "G"]
queue = [["A", "C"], ["A", "B", "D"], ["A", "B", "G"]]


queue = [
    ["A", "C"] (POP), 
    ["A", "B", "D"], 
    ["A", "B", "G"]
], 
path = ["A", "C"], node = "C", node != end
adjacent in ["D", 'E'] - C
new_path = ["A", "C", "D"]
queue = [["A", "B", "D"], ["A", "B", "G"], ["A", "C", "D"]]
new_path = ["A", "C", "E"]
queue = [["A", "B", "D"], ["A", "B", "G"], ["A", "C", "D"], ["A", "C", "E"]]

queue = [
    ["A", "B", "D"] (POP), 
    ["A", "B", "G"], 
    ["A", "C", "D"], 
    ["A", "C", "E"]
], 
path = ["A", "B", "D"], node = "D", node != end
adjacent in ["F"] - D
new_path = ["A", "B", "D", "F"]
queue = [["A", "B", "G"], ["A", "C", "D"], ["A", "C", "E"], ["A", "B", "D", "F"]]

queue = [
    ["A", "B", "G"] (POP), 
    ["A", "C", "D"], 
    ["A", "C", "E"], 
    ["A", "B", "D", "F"]
]
path = ["A", "B", "G"], node = "G" node != end
adjacent in ["F"] - G
new_path = ["A", "B", "G", "F"]
queue = [["A", "C", "D"], ["A", "C", "E"], ["A", "B", "D", "F"], ["A", "B", "G", "F"]]

queue = [
    ["A", "C", "D"] (POP), 
    ["A", "C", "E"], 
    ["A", "B", "D", "F"], 
    ["A", "B", "G", "F"]
]
path = ["A", "C", "D"], node = "D", node != end
adjacent in ["F"] - D
new_path = ["A", "C", "D", "F"]
queue = [["A", "C", "E"], ["A", "B", "D", "F"], ["A", "B", "G", "F"], ["A", "C", "D", "F"]]

queue = [
    ["A", "C", "E"] (POP), 
    ["A", "B", "D", "F"], 
    ["A", "B", "G", "F"], 
    ["A", "C", "D", "F"]
]
path = ["A", "C", "E"], node = "E", node != end
adjacent in ["F"] - E
new_path = ["A", "C", "E", "F"]
queue = [["A", "B", "D", "F"], ["A", "B", "G", "F"], ["A", "C", "D", "F"], ["A", "C", "E", "F"]]

queue = [
    ["A", "B", "D", "F"] (POP), 
    ["A", "B", "G", "F"], 
    ["A", "C", "D", "F"], 
    ["A", "C", "E", "F"]
]
path = ["A", "B", "D", "F"], node = "F" node == end 
return path (Single Source ShortestPath)
```

`Starting Vertex`의 자식 ==> 자식 ==> 자식 ==> ... ==> `End Vertex`

모든 경로를 확인해보고, 경우의 수 중 `Starting Vertex`가 리스트의 첫 번째 요소이고, `End Vertex`가 리스트인 것이 확인되면 바로 리턴해서, 최단거리 경로를 찾는다.

## Why BFS not work with weighted graph

![img](https://cdn-images-1.medium.com/max/1000/1*bVQwju8QuUYz2nnd13hDOw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*j80nqnRc25GbSBw8racqHg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*D_o2aC_H0TMrEaVUOfxC4Q.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ffrix1lNCAbZXqj-SQtlGg.png)

위와 같이 `Weighted Graph`에서는  `BFS`를 사용할 수 없다 (정확히는 사용해도 기대값을 얻을 수 없다). 

1. `Vertex A`를 `Parent`로 갖는 `Vertex`

- B (10)
- C (20)

2. `Vertex B`를 `Parent`로 갖는 `Vertex`

- D (30)
- E (5)

문제는 `Unweighted Graph`에서는 A ==> H로 가는 최단 경로를 찾을 때, 

A ==> B ==> D ==> H 경로를 선택할 것이다. 

하지만, 위 사진의 `Weighted Graph` 

B ==> E ==> D ==> H 경로가 최단 경로이다.

이러한 이유 때문에 `Weighted Graph` 에서는 `BFS`를 사용할 수 없다.

## Why does DFS not for SSSP?

DFS has the tendency to go "as far as possible" from source, hence it can never find "Shortest Path".

![img](https://cdn-images-1.medium.com/max/1000/1*7HN7Iw0lQALDiR189zG3cg.png)

`DFS`는 깊이 우선 탐색 방식으로 동작하기 때문에, 최단 경로를 찾는데 사용하기 적합하지 않다. 위 사진처럼 `DFS`는 시작점으로부터 가능한 멀리 떨어져, 깊이 우선으로 탐색을 한다. 

만약 `A ==> C`로 가는 경로를 찾을 때 `DFS`를 사용한다면 아래 순서로 `C`로 가는 경로를 탐색할 것이다. 이것은 경로를 찾는 관점에서는, 최악의 경우의 수로 볼 수 있기 때문에, `DFS`는 최단 경로에 적합하지 않다.

**A ==> B ==> D ==> E ==> I ==> F ==> C**























