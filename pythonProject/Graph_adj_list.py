# Adjacency list representation:-------linked list

# Creating Vertex of graph.

class AdjNode:

    def __init__(self, data):
        self.vertex = data
        self.next = None


# Creating  Graph:

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices  # this will create the list of size = Num. of vertices.
        # list will be used to store the linked list of nodes.

    def add_edge(self, src, dest):
        # Adding source to destination.
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding destination to source.
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            temp = self.graph[i]
            print("Adjacency list of vertex {}\n head".format(i), end="")
            while temp:
                print(" --> {}".format(temp.vertex), end=" ")
                temp = temp.next
            print()


graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
graph.print_graph()
