import sys
 
p = int(input())
for i in range(p):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
