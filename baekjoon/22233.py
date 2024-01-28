import sys

input = sys.stdin.readline

m, n =map(int,input().rstrip().split())
keyword = {}

unUse=m

for i in range(m):
    keyword[input().rstrip()]=False

for i in range(n):
    memo = input().rstrip().split(',')
    for j in memo:
        if(j in keyword):
            if(not keyword[j]):
                keyword[j]=True
                unUse-=1
    print(unUse)