import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
arr = []
check= [[[0,0,0] for _ in range(m)] for _ in range(n)]
d=[(1,0,'b'),(1,-1,'l'),(1,1,'r')]
q=deque()

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        count=0
        if(i==0):
            check[i][j][0]=check[i][j][1]=check[i][j][2]=arr[i][j]
            continue
        if(i==1):
            if j==0:
                check[i][j][0]=float("inf")
                check[i][j][1]=arr[i][j]+arr[i-1][j]
                check[i][j][2]=arr[i][j]+arr[i-1][j+1]
            elif j==m-1:
                check[i][j][2]=float("inf")
                check[i][j][0]=arr[i][j] + arr[i-1][j-1]
                check[i][j][1]=arr[i][j] + arr[i-1][j]
            else:
                check[i][j][2]=arr[i][j] + arr[i-1][j+1]
                check[i][j][0]=arr[i][j] + arr[i-1][j-1]
                check[i][j][1]=arr[i][j] + arr[i-1][j]
            continue
        if j==0:
            check[i][j][0]=float("inf")
            check[i][j][1]=arr[i][j] + check[i-1][j][2]
            check[i][j][2]=arr[i][j] + min(check[i-1][j+1][0],check[i-1][j+1][1])
        elif j==m-1:
            check[i][j][0]=arr[i][j] + min(check[i-1][j-1][1],check[i-1][j-1][2])
            check[i][j][1]=arr[i][j] + check[i-1][j][0]
            check[i][j][2]=float("inf")
        else:
            check[i][j][0]=arr[i][j] + min(check[i-1][j-1][1],check[i-1][j-1][2])
            check[i][j][1]=arr[i][j] + min(check[i-1][j][0],check[i-1][j][2])
            check[i][j][2]=arr[i][j] + min(check[i-1][j+1][0],check[i-1][j+1][1])

res=float("inf")
for i in range(m):
    res=min(min(check[n-1][i]),res)
print(res)
