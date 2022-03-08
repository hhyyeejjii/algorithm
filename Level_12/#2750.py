#수 정렬하기 2750
n = int(input())
num = []

for _ in range(n):
    num.append(int(input())) #숫자 받기

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j] : #순서 바로잡기 - bubble sort
            num[i] , num[j] = num[j] , num[i] 

for n in num:
    print(n) #print result


#버블정렬에 대해
#버블정렬이란 1번부터 마지막번까지 옆에 있는 애들끼리 순서가 맞지 않으면 교환하는 시스템
#회전의 횟수를 거듭하면서 순서를 맞추는 시스템