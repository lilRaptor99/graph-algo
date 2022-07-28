import re
from graph import Graph


# Check whether the given graph contains exactly 2 or 0 odd degree vertices.
def hasEulerPath(g: Graph):
    oddVertexCount = 0
    for u in g.graph:
        if(len(g.graph[u]) % 2 == 1):
            oddVertexCount += 1
    return oddVertexCount == 0 or oddVertexCount == 2


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


def fleurys(g: Graph):
    if(not hasEulerPath(g)):
        print("The graph does not contain an Euler Path")
        return
    eulerPath = []
    h = g.getDuplicateGraph()
    bridgeEdges = getBridgeEdges(h)

    #  Finding starting vertex - If the graph has odd vertices, it should be one of them
    startVertex = 0
    for u in h.graph:
        if(len(h.graph[u]) % 2 == 1):
            startVertex = u

    v = startVertex
    while(len(h.graph[v]) > 0):
        if(len(h.graph[v]) == 1):
            u = list(h.graph[v])[0]
            eulerPath.append(f"{v}->{u}")
            h.removeEdge(v, u)
            h.removeEdge(u, v)
            v = u
        else:
            uList = list(h.graph[v])
            i = 0
            u = uList[i]
            while(len(bridgeEdges.graph[u]) > 0):
                i += 1
                u = uList[i]
            eulerPath.append(f"{v}->{u}")
            h.removeEdge(v, u)
            h.removeEdge(u, v)
            v = u

    return eulerPath


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

print("Euler Path: ", end="")
print(fleurys(g))
