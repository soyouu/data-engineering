#배열로 구현한 환형 큐
class CircularQueue:
    def __init__(self, n):  #빈 큐 초기화
        self.maxCount = n   #인자로 주어진 최대 큐 길이 설정
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.maxCount
    
    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full') 
        self.rear = (self.rear + 1) % self.maxCount #rear에 있는 데이터를 한칸 옮겨 주고
        self.data[self.rear] = x    #본래 rear 자리에 새 데이터를 넣어준다.
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount   #front에 있는 데이터를 한칸 옮기고
        x = self.data[self.front]   
        self.count -= 1
        return x    #front에 저장돼있던 데이터를 반환한다. 
    
    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]  #front의 다음 칸에 있는 데이터를 반환한다. 