#양방향 연결 리스트로 구현한 스택
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList

class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    
    def size(self):
        return self.data.getLength()
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.popAt(self.size())
    
    def peek(self):
        return self.data.getAt(self.size()).data