n = int(input())
lost = list(map(int,input().split()))
happy = list(map(int,input().split()))
hp = 100
pleasure = 0
arr= [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if(j-lost[i-1]>0):
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-lost[i-1]] + happy[i-1])
        else:
            arr[i][j]=arr[i-1][j]

print(arr[n][100])