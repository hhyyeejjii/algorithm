#음계 2920
song = list(map(int,input().split()))

if song == sorted(song):
    print('ascending')
elif song == sorted(song,reverse=True):
    print('descending')
else:
    print('mixed')