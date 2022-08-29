class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.prev = previous  # For doubly linkedlist

    """
    This is the structure of the Node
    """


class LinkedList:
    def __init__(self):
        self.head = None

    def addNodeFront(self):
        """
        adding node at the front
        """
        new_node = Node(value=input("Enter the data..\n"))
        new_node.next = self.head
        self.head = new_node
        new_node.next = n1

    def displayNode(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def reverse_LL(self):
        if self.head is None:
            return
        else:
            current = self.head
            previous = None
            while current is not None:
                next = current.next
                current.next = previous
                previous = current
                current = next

            self.head = previous

#write a method to create a loop in ll


n1 = Node(3)  # n1 is the first node object of Node class with value 3
n2 = Node(4)  # n2 is the second node Object with value 4
n3 = Node(5)  # n3 is the third node object with value 5
n4 = Node(7)
n5 = Node(9)
n6 = Node(10)
n7 = Node(10)
n8 = Node(9)

LL = LinkedList()  # LL object created of the LinkedList class
LL.head = n1  # head pointed to n1 node
n1.next = n2  # n1 node pointed to n2 using next of Node class
n2.next = n3  # n2 node pointed to n3 using next of Node class
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

LL.displayNode()
print()
LL.reverse_LL()
print()
LL.displayNode()