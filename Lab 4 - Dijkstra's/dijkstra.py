from graph import DiGraphMatrix


def dijkstra(g: DiGraphMatrix, u: int):
    dist = [g.inf] * g.numberOfNodes
    dist[u] = 0
    prev = [None] * g.numberOfNodes
    Q = [u]
    while len(Q) > 0:
        v = Q.pop(0)
        for w in range(g.numberOfNodes):
            if dist[w] > dist[v] + g.graph[v][w]:
                dist[w] = dist[v] + g.graph[v][w]
                prev[w] = v
                Q.append(w)
    return dist, prev


# Creating the graph
print("Input graph:")
g = DiGraphMatrix(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 2, 7)
g.addEdge(2, 3, 8)
g.addEdge(3, 4, 3)
g.addEdge(3, 5, 1)
g.addEdge(4, 5, 2)
g.printGraph()

dist, prev = dijkstra(g, 0)

print("Distance: ", dist)
print("Previous: ", prev)
