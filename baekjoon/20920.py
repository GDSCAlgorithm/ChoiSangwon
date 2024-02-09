import sys
from functools import cmp_to_key

input = sys.stdin.readline

def cmpDic(a,b):
    if(a[1]<b[1]):
        return 1
    elif (a[1]>b[1]):
        return -1
    if(len(a[0])<len(b[0])):
        return 1
    elif(len(a[0])>len(b[0])):
        return -1
    if a>b:
        return 1
    else:
        return -1

N, M= map(int,input().split())
res={}
for i in range(N):
    a=input().rstrip()
    if(len(a)<M):
        continue
    if(a in res):
        res[a]+=1
    else:
        res[a]=1
res = [(k, v) for k, v in res.items()]

res.sort(key=cmp_to_key(cmpDic))
for i,j in res:
    print(i)
