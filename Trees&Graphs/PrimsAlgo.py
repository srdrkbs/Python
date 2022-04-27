import heapq
class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.graph = []


    # edges = []
    # for i in range(self.vertex + 1):
    #     edges[i] = []

    def addEdges(self,u,v,w):
        self.graph.append([u,v,w])
        self.graph.append([v,u,w])
        # edges[u].append((v,w))
        # edges[v].append((u,w))

    def primsAlgo(self,source):
        result = []
        heap = []
        visited = [0] * self.vertex
        #heapq.heapify(self.graph)
        heapq.heappush(heap,(0,source))
        x = heapq.heappop(heap)
       # print(x)
        print(self.graph)


        while heap:

            x = heapq.heappop()
            print(x)
        #     if visited[x[1]] == 1:
        #         continue
        #     visited[x[1]] = 1
        #     for i in range(len(edges[x[1]])):
        #


if __name__ == '__main__':
    g = Graph(6)
    g.addEdges(1, 2, 2)
    g.addEdges(1, 4, 1)
    g.addEdges(1, 5, 5)
    g.addEdges(4, 3, 3)
    g.addEdges(4, 5, 2)
    g.addEdges(4, 3, 3)
    g.addEdges(2, 3, 5)

    print(g.primsAlgo(1))
