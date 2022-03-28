#2751 sort으로 풀은 방식

n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)