#달팽이는 올라가고 싶다 2869
a,b,v = map(int, input().split())
sol = (v-b)/(a-b)
print(int(sol) if sol == int(sol) else int(sol)+1)