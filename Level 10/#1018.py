#체스판 다시 칠하기 1018

n, m = map(int, input().split())
list = []
l = []

for _ in range(n):
    list.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0:
                    if list[b][j] != 'W': idx1 += 1  
                    if list[b][j] != 'B': idx2 += 1
                else :
                    if list[b][j] != 'B': idx1 += 1
                    if list[b][j] != 'W': idx2 += 1
        l.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        l.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(l))                                   # 칠해야 하는 개수의 최소값
