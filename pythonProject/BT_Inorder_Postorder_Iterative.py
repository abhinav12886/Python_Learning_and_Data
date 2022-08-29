# Inorder and Postorder iterative.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

class BT_Inorder_Iter:
    def __init__(self, start):
        self.root = Node(start)

    def Inorder(self, root):
        if root is None:
            return
        current = root
        nodeStack = []

        while len(nodeStack)>0 or current is not None:
            if current is not None:
                nodeStack.append(current)
                current = current.left
            else:
                current = nodeStack.pop()
                print(current.data, end=" ")
                current = current.right

    def PostOrder(self, root): # not complete need to complete it....
        if root is None:
            return
        current = root
        nodeStack = []
        while len(nodeStack)>0 or current is not None:
            if current is not None:
                nodeStack.append(current)
                current = current.left 
            else:
                temp = nodeStack[-1]
                temp = temp.right
                if temp is None:
                    temp = nodeStack[-1]
                    nodeStack.pop()
                    nodeStack.append(temp)
                    while len(nodeStack)>0 and temp ==



tree = BT_Inorder_Iter(3)

tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

tree.Inorder(tree.root)

# ALGORITHM inorder:
# 1. Create an empty stack
# 2. initialize current node as root.
# 3. Push the current node to S and set current = current.left until it becomes null.
# 4. If current is null and stack is not empty then:
#    a) Pop the top item from stack
#    b) Print the popped item set current to popped_item.right
#    c) go to step 3
# 5. If current is null and stack is empty then we are done.  