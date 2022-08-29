class Queue:
    def __init__(self):
        self.item = []

    def enqeue(self, start):
        self.item.append(start)

    def deqeue(self):
        if len(self.item):  # checks if we have elements in queue or not
            return self.item.pop(0)

    def peek(self):
        if len(self.item):
            return self.item[0].data


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTreeBFS:
    def __init__(self, data):
        self.root = Node(data)

    def level_order(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqeue(start)
        traversal = []

        while len(queue.item) > 0:  # calculating the length of our elements
            traversal.append(queue.peek())  # appending the first element
            node = queue.deqeue()  # dequeing the first element and storing it into another variable for utilisation ahead in program

            if node.left:  # utlising node to check for its left and right child
                queue.enqeue(node.left)
            if node.right:
                queue.enqeue(node.right)

        return traversal


tree = BinaryTreeBFS(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

# print(tree.preorder(tree.root, []))
print(tree.level_order(tree.root))
