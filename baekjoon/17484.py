from collections import deque

n,m=map(int,input().split())
arr = []
check= [[0 for _ in range(m)] for _ in range(n)]
d=[(1,0,'b'),(1,-1,'l'),(1,1,'r')]
q=deque()

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(m):
    q.append((0,i,arr[0][i],'0'))
    while len(q)>0:
        ci,cj,count,direction=q.popleft()
        if check[ci][cj]==0 or check[ci][cj]>count:
            check[ci][cj]=count
        for a,b,c in d:
            if(c==direction):
                continue
            ni=ci+a
            nj=cj+b
            if(0<=ni<n and 0<=nj<m):
                q.append((ni,nj,count+arr[ni][nj],c))
print(min(check[n-1]))

    