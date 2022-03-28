#문자열 반복 2675
t = int(input())

for _ in range(t):
    r, s  = list(map(str,input().split()))
    r = int(r)
    for i in s:
        print(r*i , end='')
    print()