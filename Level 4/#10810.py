#10810번 공넣기
n, m = map(int, input().split()) # m = 넣는 줄 수 , n = 공 번호 
basket = [0]*n #n개까지 공번호, 0으로 초기화
for _ in range(m) :
    i,j,k  = map(int, input().split()) #i부터 j바구니까지 k번 번호
    for x in range(i,j+1): #i번부터 j까지니까 +1
        basket[x-1] = k #1번은 basket[0]번
for x in range(n):
    print(basket[x], end = " ") #세로줄로 결과값 출력. end 넣어주기
