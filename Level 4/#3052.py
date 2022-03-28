num = [ ]
for i in range(10):
    n = int(input())
    num.append(n % 42)
ans = set(num)
print(len(ans))