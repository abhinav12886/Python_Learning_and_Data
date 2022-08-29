class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.prev = previous


class DoublyLL:
    def __init__(self):
        self.head = None

    def addFront(self):
        new_node = Node(data=int(input("enter the data")))
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def addBefore(self):
        new_node = Node(data=int(input("enter the data")))
        pos = int(input("enter the node before which you want to add the data"))
        temp = self.head
        i = 1
        while i < pos - 1:
            temp = temp.next
            i += 1
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp.next

    # Define the append method to add elements at the end

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def deleteNode(self):
        if self.head is None:
            print("the list is empty")
        else:
            pos = int(input("enter the index position to be deleted"))


obj1 = DoublyLL()
obj1.addFront()
obj1.addFront()
obj1.addFront()
obj1.display()
obj1.addBefore()
obj1.display()
