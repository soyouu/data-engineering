#단순 연결 리스트
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):   #특정 원소 찾기(k번째)
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:  #1부터 pos-1까지 전진하면, 그때 curr가 가리키는 next 노드가 내가 리턴하려는 pos번째 노드임
            curr = curr.next
            i += 1
        return curr
    

    def traverse(self): #리스트 순회
        if not self.head:
            return []
        
        answer = []
        curr = self.head
        while curr is not None:
            answer.append(curr.data)    #curr.data = 현재 노드의 값
            curr = curr.next
        return answer
    
    def getLength(self):    #리스트의 길이 출력
        return self.nodeCount

    def insertAt(self, pos, newNode):   #원소 삽입
        if pos < 1 or pos > self.nodeCount:
            return False
        
        if pos == 1:    #삽입하려는 위치가 리스트의 처음일 때
            newNode.next = self.head    #newNode의 next가 원래 head
            self.head = newNode         #이제 newNode가 head

        else:
            if pos == self.nodeCount + 1:   #newNode를 삽입하려는 위치가 리스트의 마지막일 때
                prev = self.tail            #앞에서부터 찾아갈 필요 없이 prev는 self.tail로 설정해둠
            else:
                prev = self.getAt(pos-1)
            newNode.next = prev.next    #newNode의 next가 원래 prev의 next가 됨
            prev.next = newNode         #이제 prev의 next는 newNode가 됨

        if pos == self.nodeCount + 1:
            self.tail = newNode
        
        self.nodeCount += 1
        return True
        

    def popAt(self, pos):   #원소 삭제
        if pos < 1 or pos > self.nodeCount:     #pos가 올바른 범위의 값을 가지지 않을 때
            raise IndexError
        
        curr = self.getAt(pos)  #삭제할 노드
        
        if self.nodeCount == 1 and pos == 1:    #삭제하려는 노드가 유일한 리스트 노드일 때
            self.head = None
            self.tail = None
        
        elif pos == 1:     #삭제하려는 노드가 유일한 노드는 아니지만 맨 앞 노드일 때
            self.head = self.getAt(pos+1)
            
        else:
            prev = self.getAt(pos-1)
            
            if self.nodeCount is not pos:   #삭제하려는 노드가 유일한 노드가 아니고 맨 뒤 노드도 아닐 때(중간 어딘가 있는 노드일 때)
                prev.next = self.getAt(pos+1)   #getAt() 함수를 이용해서 앞에서부터 목표하는 노드까지 하나하나 탐색
            else:   #삭제하려는 노드가 맨 뒤 노드 일때
                self.tail = prev
                prev.next = None
                
        self.nodeCount -=1
        return curr.data
    

    def concat(self, L):    #두 리스트 연결
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
