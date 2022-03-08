#최댓값 2562

list = [ ]
for _ in range(9):
    n = int(input())
    list.append(n)

print(max(list))
print(list.index(max(list))+1)