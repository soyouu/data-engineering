#양방향 연결 리스트로 구현한 큐
from doublelinkedlist import Node, DoublyLinkedList

class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()


    def isEmpty(self):
        return self.size() == 0


    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(1, node)


    def dequeue(self):
        return self.data.popAt(self.size())


    def peek(self):
        return self.data.getAt(self.size()).data
