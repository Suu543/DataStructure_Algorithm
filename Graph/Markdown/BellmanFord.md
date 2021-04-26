# Bellman Ford Algorithm

Bellman Ford Algorithm is used to find single source shortest path problem. If there is a negative cycle, it catches it and reports its existence.

![img](https://cdn-images-1.medium.com/max/1000/1*zTS9YRurIdNUJ9wLNMncBA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*oTUKi6P_ZuLvDDz8Xqig8w.png)

![img](https://cdn-images-1.medium.com/max/1000/1*7bD9pC8cHE4d1Sk4yfMc6g.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ZPHsQywkV-31uIW4PhwflQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*fAhc2hJl0wO2fwgMmGAR8Q.png)

![img](https://cdn-images-1.medium.com/max/1000/1*9uYZy3snr6Xf3f9aNaMrow.png)

![img](https://cdn-images-1.medium.com/max/1000/1*6uqriy9H3UJPvpNaU_nnIA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*xrlD3oy0W9LCL2qjeDQ4gw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*nTO0CZ7QIEwifYpuRw0uSA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*nTO0CZ7QIEwifYpuRw0uSA.png)

## Bellman Ford Algorithm with negative cycle

![img](https://cdn-images-1.medium.com/max/1000/1*4uzPpWx31Nh0u4Lnn3AwKw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*-W9s2sMSmQVa14Re8TxmYA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*Fi9kD-5IHSsBHRNCeb-5lA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*lAwUXHzDYIlr1CytqSJ-YA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*OShFBD40iAGDtcgQ_aqrow.png)

![img](https://cdn-images-1.medium.com/max/1000/1*FB10CvAETzrVzzzlO8e1wg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ddO6qoIX1DVHP0dh1eW6DA.png)

## Why does Bellman Ford run V-1 times?

If any node is achieved better distance in previous iteration, then that better distance is used to improve distance of other vertices.

![img](https://cdn-images-1.medium.com/max/1000/1*Yaq1_5kmT8VYrt8dL-eXDg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*7XocZ--yLndfFBVX16jwbg.png)



![img](https://cdn-images-1.medium.com/max/1000/1*IFvfI3Hj25e96HKn-N-mlw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*j7sGUbfQEjkIiquGfmeWbg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*gLtVSi1irnQxFYMua4gv3A.png)

![img](https://cdn-images-1.medium.com/max/1000/1*x0rcGZ0FV1kzxdUawcTFFQ.png)

## Bellman Ford in Python

```python
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
                    f"source: {source} destination: {destination} weight: {weight}")
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
```

```python
# First Iteration
g.bellmanFord("E")
dist = {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': 0}
# source, destination, weight in self.graph
#Condition: if dist[source] != float("Inf") and dist[source] + weight < dist[destination]
vertices: 0 source: A destination: C weight: 6 - Condition: False
vertices: 0 source: A destination: D weight: 6 - Condition: False
vertices: 0 source: B destination: A weight: 3 - Condition: False
vertices: 0 source: C destination: D weight: 1 - Condition: False
vertices: 0 source: D destination: C weight: 2 - Condition: False
vertices: 0 source: D destination: B weight: 1 - Condition: False
vertices: 0 source: E destination: B weight: 4 - Condition: True
- dist['E'] != float("Inf") = True
- dist['E'] + 4 < dist["B"] = True
- dist['B'] = dist['E'](0) + weight(4) = 4
- dist = {'A': inf, 'B': 4, 'C': inf, 'D': inf, 'E': 0}
vertices: 0 source: E destination: D weight: 2
- dist['E'] != float("Inf") = True
- dist['E'] + 4 < dist["D"] = True
- dist['D'] = dist['E'] (0) + (2) = 2                
- dist = {'A': inf, 'B': 4, 'C': inf, 'D': 2, 'E': 0}

dist = {'A': inf, 'B': 4, 'C': inf, 'D': 2, 'E': 0}
-----------------------------------------------------------------------------------------
vertices: 1 source: A destination: C weight: 6 - Condition: False
vertices: 1 source: A destination: D weight: 6 - Condition: False
vertices: 1 source: B destination: A weight: 3 - Condition: True
- dist['B'] != float("Inf") = True
- dist['B'] + 3 (7) < dist["A"] (inf) = True
- dist['A'] = dist['B'](4) + 3 = 7
- {'A': 7, 'B': 4, 'C': inf, 'D': 2, 'E': 0}
vertices: 1 source: C destination: D weight: 1 - Condition: False
vertices: 1 source: D destination: C weight: 2 - Condition: True
- dist['D'] != float("Inf") = True
- dist['D'] + 2 (4) < dist['C'] (inf)
- dist['C'] = dist['D'](2) + 2 = 4
- {'A': 7, 'B': 4, 'C': 4, 'D': 2, 'E': 0}
vertices: 1 source: D destination: B weight: 1 - Condition: True
- dist['D'] != float("Inf") = True
- dist['D'] + 1 (3) < dist['B'] (4) = True
- dist["B"] = dist["D"](2) + 1 = 3
- {'A': 7, 'B': 3, 'C': 4, 'D': 2, 'E': 0}
vertices: 1 source: E destination: B weight: 4 - Condition: False
- dist['E'] != float("Inf") = True
- dist['E'](0) + 4 < dist["B"] (3) = False
vertices: 1 source: E destination: D weight: 2 - Condition: False
- dist['E'] != float("Inf") = True
- dist['E'](0) + 2 < dist["D"] (2) = False
                
dist = {'A': 7, 'B': 3, 'C': 4, 'D': 2, 'E': 0}
-----------------------------------------------------------------------------------------
# dist의 모든 key에 값이 할당 되었기 때문에 dist[source] != float("Inf") = True
# dist[source] + weight < dist[destination]의 참, 거짓 여부만 확인하면됨.
vertices: 2 source: A destination: C weight: 6
- dist["A"](7) + 6 < dist['C'] (4) - False
vertices: 2 source: A destination: D weight: 6
- dist["A"](7) + 6 < dist['D'] (2) - False                
vertices: 2 source: B destination: A weight: 3
- dist["B"](3) + 3 < dist['A'] (7) - True
- dist['A'] = dist['B'](3) + 3
- {'A': 6, 'B': 3, 'C': 4, 'D': 2, 'E': 0}
vertices: 2 source: C destination: D weight: 1
- dist["C"](4) + 1 < dist["D"] (2) - False
vertices: 2 source: D destination: C weight: 2
- dist["D"](2) + 2 < dist["C"] (4) - False
vertices: 2 source: D destination: B weight: 1
- dist["D"](2) + 1 < dist["B"] (3) - False
vertices: 2 source: E destination: B weight: 4
- dist["E"](0) + 4 < dist["B"] (3) - False
vertices: 2 source: E destination: D weight: 2
- dist["E"](0) + 2 < dist["D"] (2) - False                 

dist = {'A': 6, 'B': 3, 'C': 4, 'D': 2, 'E': 0}
-----------------------------------------------------------------------------------------
vertices: 3 source: A destination: C weight: 6
- dist["A"](6) + 6 < dist["C"] (4) - False
vertices: 3 source: A destination: D weight: 6
- dist["A"](6) + 6 < dist["C"] (4) - False
vertices: 3 source: B destination: A weight: 3
- dist["B"](3) + 3 < dist["A"] (6) - False
vertices: 3 source: C destination: D weight: 1
- dist["C"](4) + 1 < dist["D"] (2) - False
vertices: 3 source: D destination: C weight: 2
- dist["D"](2) + 2 < dist["C"] (4) - False 
vertices: 3 source: D destination: B weight: 1
- dist["D"](2) + 1 < dist["B"] (3) - False
vertices: 3 source: E destination: B weight: 4
- dist["E"](0) + 4 < dist["B"] (3) - False
vertices: 3 source: E destination: D weight: 2
- dist["E"](0) + 2 < dist["D"] (2) - False

dist = {'A': 6, 'B': 3, 'C': 4, 'D': 2, 'E': 0}
-----------------------------------------------------------------------------------------
```









