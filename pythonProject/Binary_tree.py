# recursive implementation DFS .......................

class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def preorder(self, start, traversal):  # start = tree.root; start.data = tree.root.data
        if start is None:                   # traversal = empty  list
            return

        traversal.append(start.data)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start is None:
            return
        self.inorder(start.left, traversal)
        traversal.append(start.data)
        self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start is None:
            return
        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.data)
        return traversal


"""----------------Above all three functions:- Preorder, inorder, postorder comes under DFS------------------"""

tree = BinaryTree(9)
tree.root.left = Node(6)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.right = Node(7)
tree.root.right.left = Node(2)
tree.root.right.right = Node(3)

print("Preorder tree data:-")
print(tree.preorder(tree.root, []))
print("Inorder tree data:-")
print(tree.inorder(tree.root, []))
print("Postorder tree data:-")
print(tree.postorder(tree.root, []))
