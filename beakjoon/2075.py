import heapq
import sys
input = sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in tmp:
        heapq.heappush(arr,j)
        if(len(arr)>n):
            heapq.heappop(arr)
print(arr[0])