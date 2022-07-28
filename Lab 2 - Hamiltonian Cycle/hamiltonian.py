from graph import Graph


# check if the given node is safe to add to the hamiltonian path.
# Vertex should be adjacent to the last node in the path, and it should not be in the path array
def isSafeToAdd(g: Graph, v: int, hamiltonianPath: list):
    if v in hamiltonianPath:
        return False
    return hamiltonianPath[-1] in list(g.graph[v])


# Recursive function to find the hamiltonian cycle in the given graph
def hamiltonianRec(g: Graph, hamiltonianPath: list):
    # print(f"cur: {hamiltonianPath}")
    # Base case all vertices are included in the path
    if len(hamiltonianPath) == g.numberOfNodes:
        # last node in the path must be adjacent to the first one
        return hamiltonianPath[-1] in list(g.graph[hamiltonianPath[0]])

    for v in range(1, g.numberOfNodes):
        if isSafeToAdd(g, v, hamiltonianPath) == True:
            hamiltonianPath.append(v)
            if hamiltonianRec(g, hamiltonianPath) == True:
                return True
            else:
                hamiltonianPath.pop()
    return False


if __name__ == "__main__":
    hamiltonianPath = [0]
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 0)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 1)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 2)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.printGraph()

    if hamiltonianRec(g, hamiltonianPath):
        print(f"Hamiltonian cycle exists: {hamiltonianPath}")
    else:
        print("Hamiltonian cycle does not exist in the input graph")
