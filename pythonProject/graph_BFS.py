class Node:
    def __init__(self, value):
        self.value = value
        self.adjacency_list = []  # we use adjacency term because there is no limit in adjacent nodes in graph
        # Tree have only left and right node but graph have many nodes and no root node.

        self.visited = False  # this is gonna keep a check on nodes whether we have visited it or not.
        # False - by default all the nodes are not visited.


class Graph:
    def BFS(self, node):  # node = starting node.
        queue = [node]
        node.visited = True  # updating it to 'true' means i have visited it.
        traversal = []  # used to store the result.

        while queue:    # if queue is not empty
            actualNode = queue.pop(0)  # storing popped node in queue
            traversal.append(actualNode.value)  # extracting popped node value and storing it in traversal list

            # Now we need to traverse all its adjacent elements.
            for element in actualNode.adjacency_list:    # getting all the adjacent elements
                if element.visited is False:    # checking if the element is visited or not
                    queue.append(element)   # if not appending it in queue
                    element.visited = True  # and marking it as visited

        return traversal


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjacency_list.append(node2)  # B we are appending adjacent nodes in the list, so that they get connected
node1.adjacency_list.append(node3)  # C
node1.adjacency_list.append(node4)  # D

node2.adjacency_list.append(node5)  # E
node2.adjacency_list.append(node6)  # F

node4.adjacency_list.append(node7)  # G

node3.adjacency_list.append(node1)  # because node A and C may be connected from A-C and C-A.

graph = Graph()  # creating object of graph class
print(graph.BFS(node2))  # using object of class graph calling BFS method and passing node1 as argument

# -----------------------------------------GRAPH OF ABOVE IMPLEMENTATION------------------------------
#
#                                                  A
#                                                / | \
#                                               /  |  \
#                                              B   C   D
#                                             / \     /
#                                            /   \   /
#                                           E     F G
