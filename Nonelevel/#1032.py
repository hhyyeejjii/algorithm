# 1032번 명령 프롬프트
import sys

def input():
    return sys.stdin.readline().rstrip()

def stringCompare(str1, str2):
        result = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                result.insert(i, '?')
            else:
                result.insert(i, str1[i])

        return result

n = int(input())
if n == 1:
    str = input()
    print(str)
else:
    strings = []
    for _ in range(n):
        strings.append(list(input()))

    bridge = stringCompare(strings[0], strings[1])
    if len(strings) >= 3:
        for i in range(2, len(strings)):
            bridge = stringCompare(bridge, strings[i])

    print(''.join(bridge))