#소수 찾기 19778

n = int(input())
num = map(int, input().split())
prime = 0 #소수 개수 카운팅

for i in num :
    cnt = 0
    if i == 1 : # 1 빼고 소수 구하기
        continue
    for j in range(2, i+1): 
        if (i%j == 0):
            cnt += 1
    if cnt == 1:
        prime += 1
print(prime)햐