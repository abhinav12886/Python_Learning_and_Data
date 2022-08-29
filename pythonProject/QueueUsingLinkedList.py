class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        if self.front is None:
            print("Queue list is empty")
        else:
            return

    def enqueue(self):
        new_node = Node(data=int(input("enter the data to be inserted at front of queue")))
        if self.front is None:
            self.front = new_node
            # self.rear = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("list is empty")
        else:
            temp = self.front.data
            self.front = self.front.next

        if self.isEmpty():
            self.rear = None
        return temp

    def displayNode(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


# obj = Queue()
# obj.enqueue()
# obj.enqueue()
# obj.enqueue()
# obj.displayNode()
# obj.dequeue()
# obj.displayNode()