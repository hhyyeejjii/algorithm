#10950
t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(a+b)

#10951
while True:
    try : #input stdin 유의 
        a,b= map(int, input().split()) #test 갯수 정해져있지 않아
        print(a+b)
    
    except:
        break

#10952
while True:
    a, b = map(int, input().split())
    if a == 0 & b == 0 :
        break;
    else:
        print(a+b)

# 서울에서 김서방 찾기
def solution(seoul):
      for i in range(0,len(seoul)):
        if seoul[i]=="Kim":
            return "김서방은 "+str(i)+"에 있다"

#문자열 다루기 기본
def solution(s):
    if (len(s) == 4 or len(s) == 6) & s.isdigit() == True : #isdigit = 숫자인지 판단
        return True
    else :
        return False