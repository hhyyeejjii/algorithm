#10809번 알파벳 찾기
s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print(s.find(i), end = ' ')

# find 로 이전에 푼 문제 다르게 풀기
s= list(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet :
    if i in s:
        print(s.index(i), end = ' ')
    else:
        print(-1 , end=' ')
# for 로 새로 풀음. for로 검사. 있으면 그 인덱스 출력 없으면 -1 출력