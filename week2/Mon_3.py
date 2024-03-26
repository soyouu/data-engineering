#피보나치 순열
def fibonacci(x):
    answer = 0
    if x < 2:
        return x
    else:
        return fibonacci(x-1) + fibonacci(x-2)
    return answer