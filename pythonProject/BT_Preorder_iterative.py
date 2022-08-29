class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTPreorder_Iter:
    def __init__(self, start):
        self.root = Node(start)

    def iter_preOrder(self, root):
        if root is None:
            return

        nodeStack = list()
        nodeStack.append(root)

        while len(nodeStack) > 0:
            node = nodeStack.pop()
            print(node.data, end=" ")

            if node.right:
                nodeStack.append(node.right)
            if node.left:
                nodeStack.append(node.left)


tree = BTPreorder_Iter(3)

tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.iter_preOrder(tree.root)

''' 
1) Create an empty stack nodeStack and push root node to stack. 
2) Do the following while nodeStack is not empty. 
….a) Pop an item from the stack and print it. 
….b) Push right child of a popped item to stack 
….c) Push left child of a popped item to stack
The right child is pushed before the left child to make sure that the left subtree is processed first.
'''
