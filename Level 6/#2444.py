#2444번 별찍기
n = int(input())
for i in range(1,n): #1부터 n번까지
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))