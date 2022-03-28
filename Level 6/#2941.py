#크로아티아 알파벳 2941
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
alpha = input() 
for t in a: 
    alpha = alpha.replace(t, 'a') 
print(len(alpha))
