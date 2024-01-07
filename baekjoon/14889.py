from itertools import  combinations
n=int(input())
team = [i for i in range(n)]
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
ttt=list(combinations(team,n//2)) 
res=10000000 
for i in ttt:
    team1=list(i) 
    team2=[]
    for j in range(n): 
        if(j not in team1):
            team2.append(j)
    team11 = list(combinations(team1,2)) 
    team21 = list(combinations(team2,2))
    team1res=0
    team2res=0
    for j,k in team11:
        team1res+=arr[j][k]
        team1res+=arr[k][j]
    for j,k in team21:
        team2res+=arr[j][k]
        team2res+=arr[k][j]
    tmp=abs(team1res-team2res) 
    if(tmp<res):
        res=tmp
print(res)