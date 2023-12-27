#2675번 문자열 반복
t= int(input())
for _ in range(t):
    r, s  = list(map(str,input().split()))
    r = int(r)
    for i in s:
        print(r*i , end='')
    print()
# r, s 분류해서 리스트로 받고 반복