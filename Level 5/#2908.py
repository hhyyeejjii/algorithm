#2908번 상수
a, b = input().split()
a = int(a[::-1]) ; b = int(b[::-1])
print(a) if a>b else print(b)

#[::-1]로 거꾸로 셈