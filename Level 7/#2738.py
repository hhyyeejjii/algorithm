#2738번 행렬 덧셈
n,m = map(int,input().split())
a=[]; b=[] #a, b 빈리스트
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end =' ') #띄어쓰기 포함시켜 -> 실패1
    print() #줄 바꿈
