#11720 숫자의 합
#1년 전에 sum map으로 문제 풀이
n = int(input())
print(sum(map(int,input())))

#map 말고 for문
n = int(input())
x = input()
sum = 0
for i in x:
    sum += int(i) # 빈 sum에 int(i)를 계속 더해줌
print(sum) 
