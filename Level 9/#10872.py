#팩토리얼 10872
# 재귀함수로 풀기
n = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))