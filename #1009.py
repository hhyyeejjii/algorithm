# 1009번 분산처리

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = []
b = []

for _ in range(n):
    num1, num2 = map(int, input().split())
    a.append(num1)
    b.append(num2)

for i in range(n):
    new_a = a[i] % 10

    if new_a == 0:
        print(10)
    elif  new_a in [1, 5, 6]:
        print(new_a)
    elif new_a in [4, 9]:
        if b[i] % 2 == 0:
            print((new_a ** 2) % 10)
        else:
            print(new_a)
    else:
        if b[i] % 4 == 0:
            print((new_a ** 4) % 10)
        else:
            print((new_a ** (b[i] % 4)) % 10) 
