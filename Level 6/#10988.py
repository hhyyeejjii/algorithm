#10998번 팰린드롬인지 확인하기
#역순으로 해도 같은 글자인지 확인하기
n = input()
if n == n[::-1] :
    print(1)
else: 
    print(0)

#역순을 떠올렸을 때 [::-1]이 떠올라서 그 방법으로 문제 풀이