#10813번 공 바꾸기
n, m = map(int, input().split()) # n = 바구니 갯수, m = 공 바꾸기 횟수
basket = list(range(n+1)) #0번부터 
for _ in range(m):
    i,j = map(int,input().split())
    basket[i] , basket[j] = basket[j] , basket[i] # i, j 교환
print(*basket[1:]) # *으로 데이터만, 1번부터인 이유는 0번에 0 출력