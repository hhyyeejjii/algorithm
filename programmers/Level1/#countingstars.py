#직사각형 별찍기
a, b = map(int, input().strip().split(' '))
pearl = ('*' * a + '\n') * b
print(pearl)