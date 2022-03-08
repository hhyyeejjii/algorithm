#1157번
word = input().upper() #대문자로 출력하므로 
wordlist = list(set(word))  # 입력받은 문자열에서 중복값을 제거

fre_word = []

for i in wordlist :
    fre_word.append(word.count(i)) #수를 세서 따로 저장

#최대인 값이 여러개 있나 count를 이용해 체크
if fre_word.count(max(fre_word)) >= 2 : 
    print('?')
else :
    #최대인 값의 인덱스를 구하고 해당하는 인덱스 값을 출력
    print(wordlist[fre_word.index(max(fre_word))])
    
