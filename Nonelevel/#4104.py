#크냐 4104
while True:
    a, b = map(int, input().split() )
    if a == 0 & b == 0 :
        break
    elif a > b :
        print('Yes')
    else :
        print('No')