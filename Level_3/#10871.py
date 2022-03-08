#x보다 작은 수 10871

n,x = map(int, input().split())
a = list(map(int,input().split()))
for i in range(n):
    if a[i] < x :
        print(a[i], end= ' ') #end 한칸 공백 설정
