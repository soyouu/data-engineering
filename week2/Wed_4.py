#중위표현수식 -> 후위표현수식
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

#연산자의 우선 순위 설정:: '('도 연산자로 취급
prec = {    
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
} 


def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for op in S:
        if op == ")":   #스택에서 닫는 괄호를 만날 경우
            while opStack.peek() != "(":    #여는 괄호를 만나지 않으면
                answer += opStack.pop()     #pop 수행(즉, 여는 괄호를 만날 때까지)
            opStack.pop()   #여는 괄호를 만나면, 스택에 있는 여는 괄호 pop
        elif op not in prec:    #닫는 괄호도 아니고, 연산자도 아닌 경우(숫자일 때)
            answer += op    #answer 배열에 추가
        else:   #스택이 비어 있는 경우 or 연산자를 만난 경우
            if opStack.isEmpty():   #스택이 비어 있는 경우
                opStack.push(op) #스택에 op push
            else:   #스택에 연산자들이 있는 경우
                if prec[opStack.peek()] < prec[op] or op == "(":    #현재 연산자(op)의 우선 순위가 스택의 top에 있는 연산자의 우선 순위보다 큰 경우
                    opStack.push(op)                                #스택에 넣기
                else:   #스택에 있는 연산자들이 현재의 연산자보다 우선 순위가 더 큰 경우
                    while not opStack.isEmpty():    #스택이 빌 때까지
                        if prec[opStack.peek()] >= prec[op]:   
                            answer += opStack.pop() #모두 pop
                        else:
                            break
                    opStack.push(op)
    while not opStack.isEmpty():
        answer += opStack.pop()
                    
    return answer