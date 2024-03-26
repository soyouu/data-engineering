#dummy head를 가지는 연결 리스트
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
    
class LinkedList2:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail
    
    def getLength(self): #리스트의 길이 출력
        return self.nodeCount
    
    def traverse(self): #리스트 순회
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next    #먼저 그 다음 노드를 방문한 후
            result.append(curr.data)    #노드의 데이터를 꺼내서 리스트에 추가
        return result
    
    def getAt(self, pos):   #특정 원소 찾기(k번째)
        if pos < 0 or pos > self.nodeCount:
            return None
    
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr
    
    def insertAfter(self, prev, newNode):   #prev의 next에 원소 삽입
        newNode.next = prev.next
        if prev.next == None:   #prev가 tail일 때
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True
    
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount:
            return False
        
        if pos != 1 and pos == self.nodeCount + 1:  #pos=1이고, pos=self.nodeCount+1이면 그건 빈 리스트에 삽입하는 경우가 되기 때문에 'pos != 1'라는 조건을 추가
            prev = self.tail
        else:       #그렇지 않은 경우(삽입하려는 위치가 마지막이 아닌 경우), 처음인지 아닌지는 상관하지 않는다. 
            prev = self.getAt(pos-1)
        return self.insertAfter(prev, newNode)
    
    def popAfter(self, prev):   #prev의 next 원소를 삭제
        curr = prev.next
        if prev.next == None:   #prev가 마지막 노드일 때
            return None         #삭제할 노드 없음 
        
        if curr.next == None:   #삭제할 노드가 리스트 마지막 노드일 때
            self.tail = prev
            prev.next = None
        else:
            prev.next = curr.next

        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        prev = self.getAt(pos-1)
        return self.popAfter(prev)  #앞서 구현한 popAfter()를 호출하므로 훨씬 간단하게 구현 가능