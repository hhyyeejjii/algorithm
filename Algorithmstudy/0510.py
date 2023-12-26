#팰린드롬수 1259
while True:
    n = input()
    if n == '0' : 
        break
    if n == n[::-1] :
        print('yes')
    else : print('no')

#영화감독 숌
n = int(input())
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):
        cnt += 1
    if cnt == n:
        print(six_n)
        break
    six_n += 1

#랜선 자르기 1654
k,n= map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
start = 1
end = max(line)
 
while(start<=end):
    mid = (start+end)//2
    cnt = 0
    for i in line:
        cnt += i//mid
    if cnt>=n:
        start = mid+1
    else:
        end = mid-1
print(end)


#나누어떨어지는숫자배열
def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if not answer : answer.append(-1)
    answer.sort()
    return answer

#같은숫자는시러
def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        if i == 0: 
            answer.append(arr[i]) 
        elif arr[i] != arr[i-1]: 
            answer.append(arr[i])
        
    print('Hello Python')
    return answer