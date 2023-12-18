#25304번 영수증
x = int(input())
n = int(input())
sum = 0
for i in range(n):
    price, count = map(int, input().split())
    sum += price * count

if sum == x :
    print("Yes")
else:
    print("No")