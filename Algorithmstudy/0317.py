#알람 시계 2884
h, m = map(int,input().split())
if m > 44:
    print(h, m-45)
elif m <45 and h>0:
    print(h-1,m+15)
else:
    print(23,m+15)

#상수 2908
a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if a > b :
    print(a)
else :
    print(b)

#음계 2920
song = list(map(int,input().split()))

if song == sorted(song):
    print('ascending')
elif song == sorted(song,reverse=True):
    print('descending')
else:
    print('mixed')

#programmers

#자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    reverse = reversed(str(n))
    for i in reverse:
        answer.append(int(i))
    return answer

#자릿수 더하기
def solution(n):
     return sum(map(int,str(n)))