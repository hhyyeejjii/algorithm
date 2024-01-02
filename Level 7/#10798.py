#10798번 세로읽기
words = []
for i in range(5): 
    word = input()
    words.append(word)

for i in range(15): #최대 15자
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='') #[0][0] 다음 [1][0]