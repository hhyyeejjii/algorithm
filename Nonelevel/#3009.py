#네번째 점 3009
xlist = []
ylist = []
for i in range(3):
    x,y = map(int,input().split())
    xlist.append(x) ; ylist.append(y) #x, y값 3줄 리스트에 저장
for i in range(3):
    if xlist.count(xlist[i]) == 1 :
        X = xlist[i]
    if ylist.count(ylist[i]) == 1 :
        Y = ylist[i] #같은건 이미 있으니까 개수가 하나인걸 출력
print(X,Y)