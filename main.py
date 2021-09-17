from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        # defaultdict is the same as the ordinary dictionary the only difference is when you try to access
        # an item that is not in the dict it by default add it to the dictionary and give it a
        # default value
        # ==> default dictionary to store the graph
        self.graph = defaultdict(list)

    def addEdge(self, parentVertex, newVertex):
        """
        adding anew edge to the graph
        :param parentVertex: the parent vertex we want to connect a new vertex with it.
        :param newVertex: the new vertex
        """
        self.graph[parentVertex].append(newVertex)

    def breadth_first_search(self, source):
        visited = []
        searchQueue = deque()
        searchQueue.append(source)
        while searchQueue:
            currentVertex = searchQueue.popleft()
            if currentVertex not in visited:
                visited.append(currentVertex)
                searchQueue += self.graph[currentVertex]
        return visited


graph = Graph()
graph.addEdge(6, 5)
graph.addEdge(5, 6)
graph.addEdge(6, 10)
graph.addEdge(10, 6)
graph.addEdge(10, 4)
graph.addEdge(4, 10)
graph.addEdge(4, 5)
graph.addEdge(5, 4)
graph.addEdge(5, 3)
graph.addEdge(3, 5)
graph.addEdge(3, 22)
graph.addEdge(22, 3)
graph.addEdge(22, 8)
graph.addEdge(8, 22)
graph.addEdge(8, 5)
graph.addEdge(5, 8)
graph.addEdge(1, 5)
graph.addEdge(5, 1)
graph.addEdge(22, 1)
graph.addEdge(1, 22)
"""
    undirected graph
  6 ----- 5 -------3--------- 22 ---------8 // source
  |       |                   |           |
  |       |                   |           |
  |       |                   |           |
  10 ---- 4                   1 --------- 5
  expected output: [8, 22, 5, 3, 1, 5, 6, 4, 10]
"""

print(graph.breadth_first_search(8))
