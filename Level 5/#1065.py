# 한수 1065
from itertools import count


def hansu(n) :
    count = 0
    for i in range(1, n+1):
        if 0< i < 100:
            count += 1  # 100보다 작으면 모두 한수
        elif i == 1000 :
            pass
        else :
            hansu_list = list(map(int,str(i)))
            if hansu_list[1] == (hansu_list[0] + hansu_list[2]) /2 : # 등차수열 가운데수 공식
                count += 1
    return count

num = int(input())
print(hansu(num))