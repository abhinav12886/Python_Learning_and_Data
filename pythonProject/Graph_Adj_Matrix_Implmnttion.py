import numpy as np


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_Mat = np.zeros((vertices, vertices))  # it will create a (vertices * vertices) matrix

    def insert_edge(self, u, v, x=1):  # by default x(weight of edge) will be 0
        self.adj_Mat[u][v] = x

    def remove_edge(self, u, v):
        self.adj_Mat[u][v] = 0  # we are making it 0

    def exist_edge(self, u, v):
        return self.adj_Mat[u][v] != 0

    def vertex_count(self):
        return self.vertices

    def edge_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj_Mat[i][j] != 0:
                    count += 1
        return count

    def vertices1(self):  # prints all the vertices present in the graph
        for i in range(self.vertices):
            print(i, end=' ')
        print()

    def edges(self):  # prints all the edges present in the graph
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj_Mat[i][j] != 0:
                    print(i, '--', j)

    def out_degree(self, v):  # prints all the edges outgoing from the given vertex present in the graph
        count = 0
        for j in range(self.vertices):
            if self.adj_Mat[v][j] != 0:
                count += 1
        return count

    def in_degree(self, v):  # prints all the edges incoming from the given vertex present in the graph
        count = 0
        for i in range(self.vertices):
            if self.adj_Mat[i][v] != 0:
                count += 1
        return count

    def display_adjMat(self):
        print(self.adj_Mat)

    def BFS(self, start_vertex):
        i = start_vertex
        q = []
        visited = [0] * self.vertices  # every node is not visited.
        print(i, end=' ')
        visited[i] = 1  # marking node as visited.
        q.append(i)
        while q:
            i = q.pop(0)
            for j in range(self.vertices):
                if self.adj_Mat[i][j] == 1 and visited[j] == 0:
                    print(j, end=' ')
                    visited[j] = 1  # marking the node to be visited.
                    q.append(j)


G = Graph(10)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Vertices: ', G.vertex_count())
G.insert_edge(0, 1)  # for weighted undirected graph just pass the third argument also 'G.insert_edge(0, 1, 26)'
# where 26 is the weight of the edge.
G.insert_edge(0, 2)
G.insert_edge(1, 2)
G.insert_edge(2, 3)
G.insert_edge(3, 6)
G.insert_edge(3, 8)
G.insert_edge(1, 9)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Edges Count:', G.edge_count())
print('Vertices:')
G.vertices1()
print('Edges:')
G.edges()
print('Edges between 1--3:', G.exist_edge(1, 3))
print('Edges between 1--2:', G.exist_edge(1, 2))
print('Edges between 2--1:', G.exist_edge(2, 1))
print('Degree of vertex 2:', G.in_degree(2) + G.out_degree(2))
print('In-Degree of vertex 2:', G.in_degree(2))
print('Out-Degree of vertex 2:', G.out_degree(2))
print('Graph Adjacency Matrix')
G.display_adjMat()
G.remove_edge(1, 2)
print('Graph Adjacency Matrix')
G.display_adjMat()
print('Edges between 1--2:', G.exist_edge(1, 2))
print("BFS Traversal:- ")
G.BFS(0)
