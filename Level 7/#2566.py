#2566번 최댓값
table = [list(map(int, input().split())) for _ in range(9)] #9*9로 받음

max_num = 0
max_i, max_j = 0, 0
for i in range(9):
    for j in range(9):
        if max_num <= table[i][j]:
            max_i = i + 1
            max_j = j + 1
            max_num = table[i][j]

print(max_num)
print(max_i, max_j)