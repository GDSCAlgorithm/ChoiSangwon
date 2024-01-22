import sys

input = sys.stdin.readline

m, n =map(int,input().rstrip().split())
keyword = {}

unUse=m

for i in range(m):
    keyword[input().rstrip()]=0

for i in range(n):
    memo = input().rstrip().split(',')
    for j in memo:
        if(j in keyword):
            if(keyword[j]==0):
                keyword[j]+=1
                unUse-=1
    print(unUse)