import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

def binary(a,b):
    start = 0
    end = N - 1
    if(b):    
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < a:
                start = mid + 1
            else:
                end = mid -1
        return end+1
    else:
        while start <= end:
            mid = (start + end) // 2
            if a<arr[mid]:
                end = mid -1
            else:
                start = mid + 1
        return end

for i in range(M):
    a,b=map(int,input().split())
    print(binary(b,False)-binary(a,True)+1)