#우선순위 큐 구현
from doublelinkedlist import Node, DoublyLinkedList

class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()
    
    def size(self):
        return self.queue.getLength()
    
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr.next != self.queue.tail and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data