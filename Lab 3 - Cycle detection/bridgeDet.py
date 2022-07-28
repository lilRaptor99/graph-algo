from graph import Graph


def dfsUtil(g: Graph):  # Do DFS and return visited vertex list
    visited = []
    dfsRec(0, g, visited)
    return visited


def dfsRec(u: int, g: Graph, visited: list):  # DFS recursive function
    visited.append(u)
    for v in g.graph[u]:
        if(not v in visited):
            dfsRec(v, g, visited)


def getBridgeEdges(g: Graph):
    bridgeEdges = Graph(g.numberOfNodes)
    h = g.getDuplicateGraph()
    for u in g.graph:
        vs = g.graph[u].copy()
        for v in vs:
            h.removeEdge(u, v)
            if(len(dfsUtil(h)) < g.numberOfNodes):  # removing u,v disconnects the graph
                bridgeEdges.addEdge(u, v)
                bridgeEdges.addEdge(v, u)
            h.addEdge(u, v)

    return bridgeEdges


# Creating the graph
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 3)
g.addEdge(4, 5)
g.addEdge(5, 3)
g.addEdge(5, 4)
g.printGraph()

bridgeEdgeGraph = getBridgeEdges(g)

print("\nBridge edges: ")
print(bridgeEdgeGraph.printGraphCompact())
