#이진 트리의 구현
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
    
class Node:
    def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1
    
    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        if (r > 1):
            return r + 1
        else:
            return l + 1
    
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
        
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
        
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def bft(self):  #넓이 우선 순회  - 재귀적 방법이 적합하지 않음
        traversal = []  #빈 리스트로 traversal 초기화
        q = ArrayQueue()    #빈 큐 

        if self.root:   #빈 트리가 아니면
            q.enqueue(self.root)    #루트 노드를 q에 추가

        while q.size() != 0:    #q가 빈 큐가 될 때까지 반복
            node = q.dequeue()  #q에서 원소를 추출
            traversal.append(node.data) #노드를 방문
            if node.left:   #노드의 왼쪽, 오른쪽 자식들이 있으면, q에 추가
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        #q가 빈 큐가 되면 모든 노드 방문 완료
        return traversal

