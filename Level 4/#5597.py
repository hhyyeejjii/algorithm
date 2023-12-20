#5597번 과제 안 내신 분 .. ?
list = [ i for i in range(1,31)] #30개니까 31까지
for _ in range(28):
    a = int(input())
    list.remove(a)
print(min(list)) ; print(max(list))