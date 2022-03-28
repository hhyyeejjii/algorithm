#병합 정렬 사용
#병합 정렬이란 하나의 문제를 두개로 분리하고 해결하여 다시 합치는 방법
#이 문제에서는 수를 쪼개어 각자의 순서대로 맞추는 행위를 반복
def merge_sort(array):
    if len(array)<=1:
        return array
    center = len(array)//2
    right = merge_sort(array[center:]) #center을 중심으로 쪼개서 right는 center부터
    left = merge_sort(array[:center]) #left는 center 전까지

    i, j, k = 0,0,0
    list = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i]) #작은 수 리스트에 append하고
            i+=1 #수를 한 개 더 가져와 비교
        else:
            list.append(right[j])
            j+=1
    
    list += left[i:]
    list += right[j:] #while문 빠져나왔을 때의 요소를 리스트에 넣기
    return list

num = int(input())
list = []

for _ in range(num):
    list.append(int(input()))
list = merge_sort(list)

for i in list :
    print(i)

#pypy3이 python3의 실행에서 시간이 오래 걸린다는 점을 바꾼 방식이기에 pypy3으로 sort 다시 도전해보기