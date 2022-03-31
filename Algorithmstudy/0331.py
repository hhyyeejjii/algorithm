#10171
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

#10172
print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

#10809
n = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(n.find(i), end = ' ')

#시저암호
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

#문자열을 정수로 바꾸기
def solution(s):
    return int(s)