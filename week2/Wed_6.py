#배열로 구현한 큐
class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self): #큐의 맨 앞 원소 찾기
        return self.data[0]