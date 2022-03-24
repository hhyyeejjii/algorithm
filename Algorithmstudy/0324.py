#3052
num = [ ]
for i in range(10):
    n = int(input())
    num.append(n % 42)
ans = set(num)
print(len(ans))

#8958
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)

#9498
x=int(input())
if x>=90 : print('A')
elif x>=80 : print('B')
elif x>=70 : print('C')
elif x>=60 : print('D')
else : print('F')

#programmers

#이상한 문자 만들기
def solution(s):
    answer = []
    s = s.split(' ') #단어 공백 기준
    
    for i in range(len(s)): 
        result = '' #''.append
        
        for j in range(len(s[i])):
            result += s[i][j].upper() if j % 2 == 0 else s[i][j].lower()
        answer.append(result)
    return ' '.join(answer)

#약수의 합
def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])