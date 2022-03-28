#벌집 2292

n = int(input())
count = 1
count_six = 6
cnt = 1
while n > count :
    cnt += 1
    count += count_six
    count_six += 6
print(cnt)