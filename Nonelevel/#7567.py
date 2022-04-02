#그릇 7567

dishes = list(str(input()))
cm = 0
for i in range(len(dishes)):
    if i == 0 : cm += 10 #안넣었다가 실패함
    elif dishes[i] == dishes[i-1] :
        cm += 5
    else : cm += 10

print(cm)

