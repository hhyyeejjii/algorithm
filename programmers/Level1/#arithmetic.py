#x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [i * x + x for i in range(n)]