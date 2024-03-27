#후위 표현 수식 계산
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

#수가 문자열로 주어져 있을 때(몇자리 수인지 모르는 상태)
#각각을 피연산자인 수와 연산자인 기호로 분리해서 리스트로 만드는 함수
#exprStr: 중위 표현식으로 된 수식
def splitTokens(exprStr):
    tokens = []
    val = 0 #각 자리 숫자를 담는 변수
    valProcessing = False
    for c in exprStr:
        if c == ' ':    #빈칸은 그냥 넘어감
            continue
        if c in '0123456789':   #숫자를 만나면
            val = val * 10 + int(c) #10진수로 변환하는 과정
            valProcessing = True
        else:   #숫자가 아니라면(괄호 또는 연산자를 만났다면)
            if valProcessing:
                tokens.append(val)  #10진수 표현이 끝난 것으로, 리스트에 그 수를 포함하고 val값 초기화
                val = 0
            valProcessing = False   #지금 10진수를 처리하고있지 않다는 뜻
            tokens.append(c)
    if valProcessing:   #마지막 수 처리
        tokens.append(val)

    return tokens

#중위 표기법 -> 후위 표기법 바꾸는 함수
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []    #Wed_4와 달리 문자열이 아니라 리스트에 추가
    
    for token in tokenList:
        if type(token) is int:  #숫자이면 리스트에 추가
            postfixList.append(token)
        elif token == "(":      #"("이면 스택에 push
            opStack.push(token)
        elif token == ")":      #")"이면 "("가 나올 때까지 pop
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            opStack.pop()
        else:   #연산자이면
            if opStack.isEmpty():   #스택이 비어잇는 경우 스택에 push
                opStack.push(token)
            else:       #스택이 비어있지 않다면 연산자의 우선순위 비교
                while not opStack.isEmpty():    #스택에 값이 존재할 동안에 계속 반복
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(token)        
    while not opStack.isEmpty():    #반복문을 다 돌고 스택이 빌 때까지 모두 pop
        postfixList.append(opStack.pop())
        
    return postfixList  #리스트로 리턴

#후위 표현 수식 계산 함수
def postfixEval(tokenList):
    valStack = ArrayStack()
    
    for token in tokenList:
        if type(token) is int:  #피연산자를 만나면 스택에 push
            valStack.push(token)
        
        #연산자를 만나면
        elif token == '*':
            a1 = valStack.pop()
            a2 = valStack.pop()
            valStack.push(a2*a1)
            
        elif token == '/':
            a1 = valStack.pop()
            a2 = valStack.pop()
            valStack.push(int(a2/a1))
            
        elif token == '+':
            a1 = valStack.pop()
            a2 = valStack.pop()
            valStack.push(a2+a1)  
            
        elif token == '-':
            a1 = valStack.pop()
            a2 = valStack.pop()
            valStack.push(a2-a1)
            
    return valStack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val