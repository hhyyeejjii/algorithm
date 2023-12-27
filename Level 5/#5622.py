#5622번 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for j in range(len(a)):
    for i in dial: #alpabet 요소에서 한글자씩 분리
        if a[j] in i: #문자를 분리
            time += dial.index(i)+3
print(time)
# 1년전 풀이와 다르게 풀어보기. 3을 미리 더하고 시작해보자
dial_d = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}
a = input()
time = 0
for x in a:
    for y,z in dial_d.items():
        if x in y :
            time += z
print(time)
