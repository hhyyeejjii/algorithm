#숫자의 개수 2577

a =int(input())
b =int(input())
c =int(input())

n =a*b*c
n_list = list(str(n))
for i in range(10):
    n_num_count = n_list.count(str(i))
    print(n_num_count)