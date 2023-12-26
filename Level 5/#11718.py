#11718번 그대로 출력하기
#while 문 작성
while True:
    try:
        print(input())
    except EOFError:
        break

# END OF FILE Error 일때 멈추기