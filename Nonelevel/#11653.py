#소인수분해 11653

from re import I


n = int(input())
i = 2
while n!=1 :
    if n%i == 0 :
        n = n/i
        print(i)
    else : i+=1