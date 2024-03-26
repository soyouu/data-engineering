#피보나치 순열
def solution(x):
    answer = 0
    if x < 2:
        return x
    else:
        return solution(x-1) + solution(x-2)
    return answer