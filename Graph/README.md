## Graph Algorithms

1. What is a graph? Why do we need it?
2. Graph Terminologies
3. Types of graphs. Graph Representation
4. Traversal of graphs. (BFS AND DFS)
5. Topological Sorting
6. Single source shortest path (BFS, Dijkstra and Bellman Ford)
7. All pairs shortest path (BFS, Dijkstra, Bellman Ford and Floyd Warshall algorithms)
8. Minimum Spanning Tree (Kruskal and Prim algorithms)

## What is Graph?

Graph consists of a finite set of Vertices(or nodes) and a set of Edges which connect a pair of nodes.

![img](https://cdn-images-1.medium.com/max/1000/1*9WcPtVwP6skX6prwK4hiqQ.png)

Why do we need it?

Graphs are used to solve various real life problems. For example, graphs are used to represent networks. The networks may include in a city or telephone network or circuit network. Graphs are also used in social networks like LinkedIn, Facebook.

Now let's say we are giving a problem called shortest path between cities.

![img](https://cdn-images-1.medium.com/max/1000/1*EURZjgA10iYQPpA5KZcYjg.png)

Here you can see that from London, you have different flights to different cities.

Let's say if you want to go to from London to Baku, we have different paths.

We don't have direct flight to go to Baku. To go Baku, 

- we can fly to Moscow, then come to Baku.
- we can fly to Kyiv, then come to Baku.
- we can fly to Istanbul, then come to Istanbul.

The question is that how we identify the shortest path to Baku from London.

Tree data structure may solve this problem because tree data structure has nodes and this nodes are connected with path. Part of the problem with this data structure is that it does not have cycle there. But here in this map, you can easily see that we have cycle over here.

For example, 

when we travel from London to Moscow, then travel to Baku, and

from Baku, we can travel to Istanbul and back to London. 

So here we have a circular path over here. Therefore, this case cannot be handled in case of tree, because tree can't handle the cycle.

The only option is graph data structure.

In a typical graph, we have Vertices(or nodes)  and edges. So we can represent these cities and connect them with edges. And the edge will be the path between these cities and we can calculate the cost of this path and set them as a way. So after doing so, we can solve the problem of shortest path.

## Graph Terminology

- **Vertices (vertex)** - Vertices are the nodes of the graph
- **Edge** - The edge is the line that connects pairs of vertices
- **Unweighted graph** - A graph which does not have a weight associated with any edge
- **Weighted graph** - A graph which has a weight associated with any edge
- **Undirected graph** - In case the edges of the graph do not have a direction associated with them
- **Directed graph** - If the edges in a graph have a direction associated with them
- **Cyclic graph** - A graph which has at least one loop
- **Acyclic graph** - A graph with no loop
- **Tree** - It is a special case of directed acyclic graph



![img](https://cdn-images-1.medium.com/max/1000/1*ZexiMteN-aQwG416WzV3QQ.png)

**Vertices (vertex)**

![img](https://cdn-images-1.medium.com/max/1000/1*yMxpFVAQ4caiRjf7xEYqtg.png)

**Edge**

![img](https://cdn-images-1.medium.com/max/1000/1*KXiCVRa_UTyX2L_r8pHtrA.png)

**Unweighted graph**

![img](https://cdn-images-1.medium.com/max/1000/1*XiUrQSAjhO5qti5qKlgjfQ.png)

**Weighted graph**

- Travel from v1 to v2 takes eight units of time
- Travel from v1 to v4 takes twelve units of time

![img](https://cdn-images-1.medium.com/max/1000/1*KXiCVRa_UTyX2L_r8pHtrA.png)

**Undirected graph**

- Can travel from v1 to v2 or from v2 to v1
- We don't have any restriction for traveling between these verses over here

![img](https://cdn-images-1.medium.com/max/1000/1*ipdtT6bZ8Xxy4wspCDuK7A.png)

**Directed graph**

- Can travel from v1 to v2
- Cannot travel from v2 to v1
- Can travel from v1 to v4
- Cannot travel from v4 to v1
- If you want to go from if we want, we need to try another path that exists over there

![img](https://cdn-images-1.medium.com/max/1000/1*xNmM0beypGJaE3h-7Ev3lg.png)

**Cyclic graph (하나 이상의 중복된 경로 없이 시작점으로 돌아오는 경우)**

- We can go from v1 to v2, then v2 to v4, then come back to the one, so here you see that we have a cycle

- If we have at least one cycle in this graph, it is called cyclic graph

- Another cyclic is that we can go from v1 to v4, then v4 to v5, then v5 to v3, then come back to the one. In this case we have another cycle here.

  ![img](https://cdn-images-1.medium.com/max/1000/1*OAjZyTwvdg0lDBK6b88G3A.png)

**Acyclic graph**

- We don't have any cycle over here
- We can go from v2 to v1, then v1 to v3, then v3 to v5, but we cannot come back to v2 through different paths, but we come back with the same paths.

![img](https://cdn-images-1.medium.com/max/1000/1*aNfWoLMraoftlO1hX3UQeg.png)

**Tree**

- Tree is a special case of directive acyclic graph. 
- We can see that it's directed. 
- We can travel from v1 to v2, but we cannot come back from v2 to v1.

- We can travel from v1 to v3, then v3 to v5, but we cannot come back from v5 to v3 or v3 to v1.
- This is acyclic because there is no loop in this graph.

## Graph Types

![img](https://cdn-images-1.medium.com/max/1000/1*EHXPCXJ5UTTNvUa5hTyUzQ.png)

1. **Unweighted - Undirected Graph**

- V1 ==> v2, v2 ==> v1, v1 ==> v4, v4 ==> v1, etc

![img](https://cdn-images-1.medium.com/max/1000/1*KXiCVRa_UTyX2L_r8pHtrA.png)

2. **Unweighted - directed Graph**

![img](https://cdn-images-1.medium.com/max/1000/1*gBXtZBrwwoeLyqxFZQlykg.png)

- v1 ==> v2 (o), v2 ==> v1 (x), v2 ==> v4 (o), v4 ==> v2 (x), etc (Undirected)
  - v1 <==> v4  (it specifies that we have two directions over here)

3. **Positive - weighted - undirected**

![img](https://cdn-images-1.medium.com/max/1000/1*Xw1s8ANRej8CCdCsLqP2qg.png)

- Weighted - if graphs have weights associated with them.

- Positive - if these weights are positive number.
- Undirected -  Do not have any direction with them.

4. **Positive - weighted - directed**

![img](https://cdn-images-1.medium.com/max/1000/1*zqrGaxLiqgdOZs9hDL0QNA.png)

5. **Negative - weighted - undirected**

![img](https://cdn-images-1.medium.com/max/1000/1*-UUeakH-JXBrdPOpEfBB1Q.png)

6. **Negative - weighted - directed**

![img](https://cdn-images-1.medium.com/max/1000/1*uI2Gshfbl9RmQHi6bsYAxQ.png)



## Graph Representation

**Adjacency Matrix**

An adjacency matrix is a square matrix or you can say it is a 2D array. And the elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph

![img](https://cdn-images-1.medium.com/max/1000/1*jQFj7cpiTAab8DkZRl8TiQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*gS1p3-_6yyf_UErACkqo4A.png)

**Adjacency List**

An adjacency list is a collection of unordered list used to represent graph. Each list describes the set of neighbors of a vertex in the graph. (Linked List)

![img](https://cdn-images-1.medium.com/max/1000/1*N2cma7OEOmEFEeSbksKtow.png)

![img](https://cdn-images-1.medium.com/max/1000/1*jTStAiSk7Cbf0K0xljMDYg.png)

If a graph is complete or almost complete we should use **Adjacency Matrix**

If the number of edges are few then we should use **Adjacency List**

![img](https://cdn-images-1.medium.com/max/1000/1*Dsi8Vssb_6F-EuEqhS79yA.png)

## Create a graph using Python

![img](https://cdn-images-1.medium.com/max/1000/1*S5GNmZLGCqjqVrpIlSL2fA.png)

## Graph Traversal

![img](https://cdn-images-1.medium.com/max/1000/1*Qmt0H42eMH37E9YAGxE9Pg.png)

```python
# gdict = graph dictionary
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


customDict = {
    "a": ["b", "c"],
    "b": ["a", "b", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.addEdge("e", "c")
print(graph.gdict)
```

# BFS (Breadth First Search)

BFS is an algorithm for traversing Graph data structure. It starts at some arbitrary node of a graph and explores the neighbor nodes (which are a current level) first, before moving to the next level neighbors.

![img](https://cdn-images-1.medium.com/max/1000/1*NUAe9b_EJ90pw7R0R9kBcw.png)

If it starts from A, our traversal looks like this

![img](https://cdn-images-1.medium.com/max/1000/1*-DVvtW63mXyLYz9C46VwtQ.png)

```python
BFS

enqueue any staring vertex
while queue is not empty
	 p = dequeue()
     if p is unvisited
        mark it visited
        enqueue all adjacent
        unvisited vertices of p
```

![img](https://cdn-images-1.medium.com/max/1000/1*HnqZBNNctYcPcXcV14Di3w.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ZIfCW4Jq1T92I1HhK0j8QQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*8N2mwW_BL5fcyKff5k4RXA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ZkHu22JpZGGQqLVKysow_A.png)

![img](https://cdn-images-1.medium.com/max/1000/1*SALL0d4aHVFTrTIzF9zV3g.png)

![img](https://cdn-images-1.medium.com/max/1000/1*YVeyefl-F-tOiZvISxOP3w.png)

![img](https://cdn-images-1.medium.com/max/1000/1*uTwfcyyQg8czWDEVFtRHbA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*P_ZZhdF-LObY-8YXphErrQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*yRThgEQOOMJcp0KYYp41Ow.png)

```python
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

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


customDict = {
    "a": ["b", "c"],
    "b": ["a", "b", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["c", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.bfs("a")
```

## DFS (Depth First Search)

DFS is an algorithm for traversing a graph data structure which starts selecting some arbitrary node and explores as far as possible along each edge before backtracking

![img](https://cdn-images-1.medium.com/max/1000/1*NUAe9b_EJ90pw7R0R9kBcw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*nNDuNZkbTwGOi75yCCdJqg.png)

## Depth First Search Algorithm

![img](https://cdn-images-1.medium.com/max/1000/1*BkOMSFL7xBAi4GsGWx-dzQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*8exR2RudVjXHRVo961sQqA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*NPFgoKGjTK39iP2p_jIu0g.png)

![img](https://cdn-images-1.medium.com/max/1000/1*OlYDFzy16cgsyH6G4btcBA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*ScLfYa3EA8F81R4BzkE5RQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*gVCTGlvpCHU2Mn8v5DMZaA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*RSY-yyiKiJE2Njxwi9sKGw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*TuCKsvFEqJ8oPA8Ak2LicA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*s_Az_pMfmt-gNbfuQQ2iFg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*zsjkEhws9xxw8105BUvLLQ.png)

![img](https://cdn-images-1.medium.com/max/1000/1*6rsX45bTj_DMQjw5weGsig.png)

![img](https://cdn-images-1.medium.com/max/1000/1*YdLS34rQkCYlzanhA5s0eg.png)

![img](https://cdn-images-1.medium.com/max/1000/1*vHhqDJiX4ROrvZTkW_y24A.png)

![img](https://cdn-images-1.medium.com/max/1000/1*OCP3TMNobAWIPidSSQ2Luw.png)

![img](https://cdn-images-1.medium.com/max/1000/1*k-gI9L5J5IuzvWfysGc41Q.png)

![img](https://cdn-images-1.medium.com/max/1000/1*Lti4jyG5Jz4L-Es9wNlAoA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*-cdJS8lwI6x5VBSQrihxJw.png)

```python
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

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


customDict = {
    "a": ["b", "c"],
    "b": ["a", "b", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["c", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.dfs("a")
```

## BFS vs DFS

![img](https://cdn-images-1.medium.com/max/1000/1*lCn5IUZPq-vPNtU9X5E6EA.png)

![img](https://cdn-images-1.medium.com/max/1000/1*LB0UdOebxARjKnUvvJ6MgQ.png)



















