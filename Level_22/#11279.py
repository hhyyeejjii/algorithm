import heapq
import sys

numbers = int(sys.stdin.readline())
heap=[]

for i in range(numbers) :
    num = int(sys.stdin.readline())
    if num != 0 :
        heapq.heappush(heap, -num)
    else :
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)