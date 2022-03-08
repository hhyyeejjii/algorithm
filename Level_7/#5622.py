#다이얼 5622

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for j in range(len(a)):
    for i in dial: #alpabet 요소에서 한글자씩 분리
        if a[j] in i: #문자를 분리
            time += dial.index(i)+3
print(time)
