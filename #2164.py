#2164 번
card = int(input())
num = 2
while True :
    if (card == 1 or card == 2) :
        print(card) ; break;
    num *= 2
    if (num >= card):
        print((card-(num//2))*2) ; break