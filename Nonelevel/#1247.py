#1247번
from sys import stdin #그냥 input()을 쓰면 시간초과가 남.

for _ in range(3):
    result = 0
    N = int(stdin.readline())
    
    #N개의 정수를 저장할 리스트
    numlist = []
    
    for j in range(N):
        num = int(stdin.readline())
        numlist.append(num)
        result += num

    if result > 0:
        print("+")
    elif result < 0:
        print("-")
    else: 
        print(0)