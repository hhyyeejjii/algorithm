#10811번 바구니 뒤집기
n, m = map(int, input().split()) # m = 바구니 번호, n = 바구니 갯수
basket = [i for i in range(1, n+1)]  #배열. i포함

for x in range(m):
    i,j = map(int, input().split())
    temp = basket[i-1:j] #temp-1 = 0
    temp.reverse()
    basket[i-1:j] = temp 
#
for x in range(n):
    print(basket[x], end=" ")
