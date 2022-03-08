#분해합 2231

n = int(input()) #분해합 입력
result = 0

for i in range(1, n+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == n):        # 생성자 s와 입력값이 같다는 것은 생성자가 없다는 뜻          
        result = i                   
        break

print(result)
