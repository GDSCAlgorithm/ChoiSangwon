from collections import deque 

def solution(maps):
    maps = [list(_) for _ in maps]
    rows, cols = len(maps), len(maps[0])
    distance = [[-1 for _ in range(cols)] for _ in range(rows)]
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'L':
                q.append((i, j, 0))
                distance[i][j] = 0
    while q:
        cx, cy, dist = q.popleft()
        
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and distance[nx][ny] == -1:
                distance[nx][ny] = dist + 1
                q.append((nx, ny, dist + 1))
                
    l_dist, e_dist = -1, -1
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'S' and l_dist == -1:
                l_dist = distance[i][j]
            if maps[i][j] == 'E':
                e_dist = distance[i][j]
    
    if l_dist == -1 or e_dist == -1:
        return -1
    else:
        return l_dist + e_dist
