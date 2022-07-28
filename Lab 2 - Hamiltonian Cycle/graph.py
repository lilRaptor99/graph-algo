from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.numberOfNodes = n
        self.graph = defaultdict(set)
        for i in range(n):
            self.graph[i] = set()

    def addEdge(self, u, v):
        self.graph[u].add(v)
        # self.graph[v].add(u)

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    def addVertex(self):
        self.graph[self.numberOfNodes] = set()
        self.numberOfNodes += 1

    def printGraph(self):
        for vertex in self.graph:
            print(f'{vertex}-> {self.graph[vertex].__str__()}')

    def getDuplicateGraph(self):
        h = Graph(self.numberOfNodes)
        for u in self.graph:
            for v in self.graph[u]:
                h.graph[u].add(v)
        return h


if __name__ == "__main__":
    # Test graph
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(0, 3)
    g.printGraph()
    g.addVertex()
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.printGraph()
