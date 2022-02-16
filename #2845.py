#파티가 끝나고 난 뒤 2845
a, b = map(int, input().split())
news = list(map(int, input().split()))

for i in news:
    print(i - a*b, end = ' ') #end 마무리 해주기 
