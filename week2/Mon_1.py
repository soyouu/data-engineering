#정렬된 리스트에 원소 넣기
def insert_list(L, x):
    for i in range(len(L)):
        if x < L[i]:
            L.insert(i, x)
            return L
    L.append(x)
    return L