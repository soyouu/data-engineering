#리스트에서 원소 찾아내기
def find1(L, x):
    answer = []
    for i in range(len(L)):
        if x == L[i]:
            answer.append(i)
        if x not in L:
            answer = [-1]
    return answer
