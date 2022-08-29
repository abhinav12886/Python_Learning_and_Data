# Csll is similar to Sll with a difference that in csll last node points
# to first node and not null.

# In csll we track of last node , we do not track the head node.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLL:
    def __init__(self, last, length):
        self.last = last
        self.length = length
