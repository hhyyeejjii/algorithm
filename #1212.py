#1212번
#bin() -> 10진수를 <0b>가 앞에 붙은 2진수로 변환한다.
#int() -> 8진수를 10진수로 변환한다.
octal = int(input(), 8)
binary = bin(octal)[2:] #앞에 붙은 0b는 떼준다.
print(binary)