from queue import Queue


class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.is_directed = is_directed
        self.graph = {}

        for node in self.nodes:
            self.graph[node] = []

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        if not self.is_directed:
            self.graph[dest].append(src)

    def print_graph(self):
        for u, v in self.graph.items():
            print(u, "-->", v)

    def BFS(self, start_node):
        queue = Queue()
        visited = {}
        bfs_traversal = []
        parent = {}
        level = {}

        for node in self.graph.keys():
            visited[node] = False
            parent[node] = None
            level[node] = -1  # it will store level of each node (means distance from source node)

        visited[start_node] = True
        level[start_node] = 0
        # we will not change parent of source node because source parent is by default "NONE"....
        queue.put(start_node)

        while not queue.empty():
            node = queue.get()
            bfs_traversal.append(node)

            # explore all the adjacent nodes of q...
            for v in self.graph[node]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = node  # calculating parent of v.
                    level[v] = level[node] + 1
                    queue.put(v)

        # return bfs_traversal
        # to get shortest distance of all nodes from source node return level
        #     return level

        # shortest path from source vertex to a given vertex.
        v = input("Enter the vertex, whose shortest path you want to calculate from source node.")
        path = []
        while v is not None:
            path.append(v)
            v = parent[v]
        path.reverse()

        return path

    # def DFS(self, start_node):  # Not working need to debug
    #     def helper(src):
    #         vis[src] = True
    #         res.append(src)
    #
    #         for node in self.graph.keys():
    #             if not vis[node]:
    #                 helper(node)
    #
    #     res = []
    #     vis = {}
    #     for node in self.graph.keys():
    #         vis[node] = False
    #     helper(start_node)
    #     return res

        # src = start_node
        # # required array and dictionary
        # color = {}  # this will keep track of node which is visited or not visited.
        # # W = vertex not visited at all(initially all white)
        # # G = when we first explore the vertex
        # # B = when we had explored all the adjacent vertex of a node we change its color to black
        # parent = {}  # we will keep track of prent of each vertex
        # trav_time = {}  # we will keep track of when the node is visited.
        # # 1.when node become gray it will be start time and
        # # 2. when it will become black that time will be its end time
        # dfs_traversal = []
        #
        # # initializing..
        # for node in self.graph.keys():
        #     color[node] = "w"
        #     parent[node] = None
        #     trav_time[node] = [-1, -1]  # means node is not visited at all
        # time = 0  # since we have to keep track of each node when it's first visited.
        #
        # def dfs_util():
        #     global time
        #     color[u] = "g"  # when we first visit it.
        #     trav_time[src][0] = self.time
        #     dfs_traversal.append(src)
        #     for v in self.graph[src]:
        #         if color[v] == "w":
        #             parent[v] = u
        #             dfs_util()
        #     color[u] = "b"
        #     trav_time[u][1] = time
        #     time += 1
        #
        # return dfs_traversal


if __name__ == "__main__":
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
    graph = Graph(nodes, is_directed=True)
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("D", "E")
    graph.add_edge("D", "A")

    # graph.print_graph()
    # print(graph.BFS("A"))

    # print(graph.DFS("A"))
