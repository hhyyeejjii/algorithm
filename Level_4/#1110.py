# 1110 더하기 사이클

import sys

def input():
    return sys.stdin.readline().rstrip()

def createNewNumber(num): # num이 10보다 클 때
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    return 10 * b + c

def createSingleNumber(num): # num이 10보다 작을 때
    return 10 * num + num

n = int(input())

if n < 10:
    new = createSingleNumber(n)
else:
    new = createNewNumber(n)

count = 1
while n != new:
    if new < 10:
        new = createSingleNumber(new)
        count += 1
    else:
        new = createNewNumber(new)
        count += 1
        
print(count)
