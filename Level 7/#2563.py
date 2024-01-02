#2563번 색종이
#첫째줄에 색종이 수 둘째줄부터 색종이 위치 ((색종이 왼쪽 아래 좌표))
#전체 배경 100*100, 색종이 하나에 10*10
n = int(input()) #색종이수 받고
arr = [[0] * 101 for _ in range(101)] #도화지 100 이하
for _ in range(n):
    y1,x1 = map(int,input().split()) #왼쪽아래 좌표받음
    
    for i in range(x1, x1+10):
        for j in range(y1,y1+10):
            arr[i][j] = 1 #전체 픽셀이 0 으로 채워져 있는 100가지 도화지에서 얘가 지나가면 1로 채우는 방식 !
ans= 0
for i in arr :
    ans += sum(i) #1을 전부 더해서 넓이를 구해

print(ans)