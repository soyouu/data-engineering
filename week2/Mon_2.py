#이진탐색 알고리즘
def solution(L, x):
    answer = -1
    start = 0
    end = len(L) - 1
    
    while start <= end:
        mid = (start+end) // 2
        target = L[mid]
        
        if target == x:
            answer = mid
            break
        elif target > x:
            end = mid -1
        else:
            start = mid + 1
            
    return answer