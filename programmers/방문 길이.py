def solution(dirs):
    answer = 0
    num = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    res={}
    visited = set()
    x, y = 0, 0

    for i in dirs:
        nx, ny = x + num[i][0], y + num[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if ((x, y), (nx, ny)) not in visited:
                answer += 1
                visited.add(((x, y), (nx, ny)))
                visited.add(((nx, ny), (x, y)))
            x, y = nx, ny
    
    return answer