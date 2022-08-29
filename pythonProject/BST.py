class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left


class BinarySearchTree:
    def __init__(self, root):
        self.root = Node(root)

    # iterative search........
    def iter_search(self, start, key):
        temp = start  # reference var which will refer to the root
        while temp:
            if key == temp.data:
                return "Found"
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return "Not Found"

    # recursive search .......
    def rec_search(self, start, key):
        # base case
        if start:
            if key == start.data:
                return "Found"
            # key is greater than the root
            elif key > start.data:
                return self.rec_search(start.right, key)
            # key is smaller than the root
            elif key < start.data:
                return self.rec_search(start.left, key)
        else:
            return "Not Found"

    # Iterative insert......
    # complexity:- time = O(H) and Space = 0(1)
    def iter_insert(self, root, key):

        # Pointer to start traversing from root
        # and traverses downward path to search
        # where the new node to be inserted
        x = root

        # Pointer y maintains the trailing
        # pointer of x
        temp = None  # temp will refer to the parent to the node which we are inserting

        # Create a new Node containing
        # the new element
        n = Node(key)

        while x is not None:
            temp = x
            if key == x.data:
                return
            elif key > x.data:
                x = x.right
            elif key < x.data:
                x = x.left

        # If the root is None i.e the tree is
        # empty. The new node is the root node
        if temp is None:  # checking if tree already have a root or not
            temp = n

        # If the new key is less then the leaf node key
        # Assign the new node to be its left child
        elif key < temp.data:
            temp.left = n
            print("inserted")

        # else assign the new node its
        # right child
        else:
            temp.right = n
            print("inserted")

        # Returns the pointer where the
        # new node is inserted
        return temp

    def rec_insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.data == key:
                return root
            elif root.data < key:
                root.right = self.rec_insert(root.right, key)
            else:
                root.left = self.rec_insert(root.left, key)
        return root

    def inorder(self, start, traversal):  # inorder traversal of BST gives sorted elements......
        if start is None:
            return
        self.inorder(start.left, traversal)
        traversal.append(start.data)
        self.inorder(start.right, traversal)
        return traversal

    def preorder(self, start, traversal):
        if start is None:
            return
        traversal.append(start.data)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start is None:
            return
        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.data)
        return traversal

    def deleteNode(self, key):
        p = self.root
        pp = None  # parent of parent
        while p and p.data != key:  # if p node exist and its element not equal to e.
            pp = p  # assigning the reference of parent node i.e the reference of
            # node p to object pp
            # Now we will check the element we are trying to delete is less
            # than the element which is stored in the reference by object p
            if key < p.data:
                p = p.left
            else:
                p = p.right
        # while loop will execute till the object p reference to node we are
        # deleting and pp will be referencing its parent.
        if not p:  # we are checking if the element to be deleted is present or not.
            # if the element not present then p will be None(False) and not None will be true
            return False
        if p.left and p.right:  # handling 3rd case (two subtrees). in this case we are selecting largest element
            # from left subtree
            s = p.left
            ps = p  # we are assigning the reference to the node which we are deleting
            while s.right:
                ps = s
                s = s.right
            p.data = s.data
            p = s
            pp = ps
        c = None
        if p.left:
            c = p.left
        else:
            c = p.right
        if p == self.root:
            self.root = None
        else:
            if p == pp.left:
                pp.left = c
            else:
                pp.right = c


B = BinarySearchTree(8)
B.root.left = Node(3)
B.root.left.left = Node(1)
B.root.left.right = Node(6)
B.root.left.right.left = Node(4)
B.root.left.right.right = Node(7)

B.root.right = Node(10)
B.root.right.right = Node(14)
B.root.right.left = Node(9)

# print(B.iter_search(B.root, 39))
# print(B.iter_search(B.root, 7))
# print(B.rec_search(B.root, 39))
# print(B.rec_search(B.root, 7))
# print(B.inorder(B.root, []))
# B.iter_insert(B.root, 9)
# B.rec_insert(B.root, 89)
# print(B.inorder(B.root, []))
# print(B.preorder(B.root, []))
print(B.postorder(B.root, []))
# B.deleteNode(14)
print(B.postorder(B.root, []))
B.deleteNode(8)
print(B.postorder(B.root, []))
B.deleteNode(3)
print(B.postorder(B.root, []))

# recursive insertion algo......
# 1. Start from the root.
# 2. Compare the searching element with root, if less than root, then recursively call left
# subtree, else recursively call right subtree.
# 3. If the element to search is found anywhere, return true,
# else return false.
