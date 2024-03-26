#리스트에서 원소 찾아내기
def find1(L, x):
    answer = []
    for i in range(len(L)):
        if x == L[i]:
            answer.append(i)
        if x not in L:
            answer = [-1]
    return answer


def find2(L, x):
    answer = []
    for index, i in enumerate(L):
        print(index, i) #index는 배열 리턴 값, i는 리스트의 값
        if i == x:  #입력받은 x값과 리스트의 i값이 같으면 index값을 추가
            answer.append(index)
    if len(answer) == 0:    #answer값이 없으면 같은 값이 없는 것이므로 -1 출력
        answer.append(-1)
    return answer