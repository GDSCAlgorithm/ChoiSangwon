N = int(input())

coordinate=[]

for i in range(N):
    coordinate.append(tuple(map(int,input().split())))

max_x = max(coord[0] for coord in coordinate)
max_y = max(coord[1] for coord in coordinate)

grid = [[0 for _ in range(max_x)] for _ in range(max_y)]

for x, y in coordinate:
    for i in range(y):
        grid[i][x - 1] = 1 

grid.reverse()

res=0

for i in range(len(grid)):
    if(grid[i].count(1)==0):
        continue
    if(grid[i].count(1)==1):
        res+=1
        continue
    front_index = grid[i].index(1) + 1
    back_index = len(grid[i]) - grid[i][::-1].index(1) 
    res+=back_index-front_index+1
print(res)
