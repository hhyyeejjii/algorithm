#셀프 넘버 4673
numbers= set(range(1, 10000))
remove_set= set()
for num in numbers :
    for i in str(num):
        num += int(i)
    remove_set.add(num) # 생성자 있으면 빈 집합에 추가
self_numbers = numbers - remove_set  # remove_set 빼서 생성자 없는 것만 모으기
for self_num in sorted(self_numbers):  # 모은거 바로 제출하지 않고 sorted로 정렬하기
    print(self_num)

