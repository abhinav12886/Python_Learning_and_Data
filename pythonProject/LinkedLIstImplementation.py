class Node:
    def __init__(self, value=None, next=None, previous=None):
        """
        This is the structure of the Node
        """
        self.value = value
        self.next = next
        self.prev = previous  # For doubly linkedlist


class LinkedList:
    def __init__(self):
        """
        This is the LinkedList class constructor
        """
        self.head = None

    def addNodeFront(self):
        """
        adding node at the front
        """
        new_node = Node(value=input("Enter the data..\n"))
        new_node.next = self.head
        self.head = new_node
        # new_node.next = n1

    # def addNodeAny(self):
    #     pos = int(input("enter the position where to insert"))
    #     new_node = Node(value=int(input("enter the value to be inserted")))
    #     p = self.head
    #     i = 1
    #     while i < pos - 1:
    #         p = p.next
    #         i += 1
    #     new_node.next = p.next
    #     p.next = new_node

    def addNodeAny2(self):  # code by sir most important
        position = int(input("enter the position where to insert"))
        new_node = Node(value=int(input("enter the value to be inserted")))
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            count = 1
            while count < position - 1:
                previous = previous.next
                count += 1
            current = previous.next
            previous.next = new_node
            new_node.next = current

    def addNodeLast(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def displayNode(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next

    def deleteAtAny(self):
        key = int(input("enter the index to be deleted"))

        if self.head is None:
            print("list is empty")  # check if the list is empty or not

        current = self.head
        z = 1
        while z < key - 1:  # it will run upto the position-2 node
            current = current.next
            z += 1
        e = current.next.value  # it contains the value deleted
        current.next = current.next.next

        return e

    def deleteAtAny2(self):  # code by sir important
        position = int(input("enter the index to be deleted"))
        if position == 1:
            self.head = self.head.next
        else:
            previous = self.head
            count = 1
            while count < position - 1:
                previous = previous.next
                count += 1
            current = previous.next
            previous.next = current.next

    def get_middleNode(self):  # most important asked in interviews
        if self.head is None:
            return
        else:
            slow_ptr = self.head
            fast_ptr = self.head
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return slow_ptr.value

    def nth_Node_from_last(self, n):
        if self.head is None:
            return
        elif n <= 0:
            return None
        else:
            main_ptr = self.head
            ref_ptr = self.head
            count = 0
            while count < n:
                if ref_ptr is None:
                    return n + "is greater than the num of nodes"
                ref_ptr = ref_ptr.next
                count = count + 1

            while ref_ptr is not None:
                ref_ptr = ref_ptr.next
                main_ptr = main_ptr.next

            return main_ptr

    def nth_frm_lst(self, n):  # using approach of finding length of ll
        temp = self.head
        length = 0
        while temp.next is not None:
            temp = temp.next
            length += 1

        if n > length:
            return
        temp = self.head
        for i in range(0, length - n+1):
            temp = temp.next

        return temp.value

    def remove_duplicate_value(self):  # list has to be sorted then only work..
        if self.head is None:
            return

        current = self.head
        while current is not None and current.next is not None:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next

    def deleteFirst(self):
        if self.head is None:
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            print(temp.value)

    def deleteLast(self):
        """
        These are the different functions of linked list
        """
        if self.head is None or self.head.next is None:
            return self.head
        else:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            return current.value

    def reverse_ll(self):
        if self.head is None:
            return
        prev = None
        curr = self.head
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev
        



n1 = Node(3)  # n1 is the first node object of Node class with value 3
n2 = Node(4)  # n2 is the second node Object with value 4
n3 = Node(5)  # n3 is the third node object with value 5
n4 = Node(7)
n5 = Node(9)
n6 = Node(10)



LL = LinkedList()  # LL object created of the LinkedList class
LL.head = n1  # head pointed to n1 node
n1.next = n2  # n1 node pointed to n2 using next of Node class
n2.next = n3  # n2 node pointed to n3 using next of Node class
n3.next = n4
n4.next = n5
n5.next = n6


LL.displayNode()
print()
LL.reverse_ll()
LL.displayNode()
# LL.addNodeFront()
# LL.addNodeFront()
# print(LL.nth_frm_lst(15))
# print()
# LL.displayNode()
# LL.deleteAtAny()
# LL.displayNode()
# LL.addNodeAny()
# print(" ")
# LL.displayNode()
# print(" ")
# print("First element deleted")
# LL.deleteFirst()
# print("")
# LL.displayNode()
# print(" ")
# LL.deleteAtAny()
# print(" ")
# LL.displayNode()
# print(LL.deleteLast())
# print(" ")
# LL.displayNode()
# LL.addNodeAny2()
# LL.displayNode()
# LL.deleteAtAny2()
print(" ")
# print(LL.get_middleNode())
# LL.remove_duplicate_value()
# LL.displayNode()
