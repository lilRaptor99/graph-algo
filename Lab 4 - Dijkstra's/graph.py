class DiGraphMatrix:
    def __init__(self, n):
        self.numberOfNodes = n
        self.graph = []
        self.inf = 9999999
        for i in range(n):
            self.graph.append([self.inf] * n)

    def addEdge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def removeEdge(self, u, v):
        self.graph[u][v] = self.inf
        self.graph[v][u] = self.inf

    def printGraph(self):
        for i in range(self.numberOfNodes):
            print("[", end=" ")
            for j in range(self.numberOfNodes - 1):
                if(self.graph[i][j] != self.inf):
                    print(self.graph[i][j], end=' | ')
                else:
                    print('_', end=' | ')
            if(self.graph[i][self.numberOfNodes - 1] != self.inf):
                print(self.graph[i][self.numberOfNodes - 1], end=' ]\n')
            else:
                print('_', end=' ] \n')


if __name__ == "__main__":
    # Test graph
    g = DiGraphMatrix(4)
    g.addEdge(0, 1, 3)
    g.addEdge(0, 2, 5)
    g.addEdge(0, 3, 7)
    g.addEdge(1, 3, 3)
    g.addEdge(2, 3, 6)
    g.printGraph()
