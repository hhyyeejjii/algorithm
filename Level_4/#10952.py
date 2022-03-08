#A+B -5 10952

while True:
    a, b = map(int, input().split())
    if a == 0 & b == 0 : # 0 0 넣으면 stop
        break;
    else:
        print(a+b)