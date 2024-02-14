from collections import deque 

def solution(board):
    answer = 0
    board = [list(_) for _ in board]
    row, col = len(board), len(board[0])
    res = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    
    def slide(i,j,dr,dc):
        while True:
            ci,cj = i + dr, j + dc
            if not (0 <= ci < row and 0 <= cj < col) or board[ci][cj] == 'D':
                return ci-dr, cj-dc
            i,j=ci,cj
                

    for i in range(row):
        for j in range(col):
            if board[i][j]== 'R':
                q.append((i,j,1))
    while q:
        cx, cy, dist = q.popleft()
        res[cx][cy]=dist
        if(board[cx][cy]=='G'):
            answer=dist
            break
        for dr , dc in d:
            nx,ny=slide(cx,cy,dr,dc)
            if(res[nx][ny]==0):
                res[nx][ny]=1
                q.append((nx,ny,dist+1))
    
    if(answer==0):
        return -1
    else:
        return answer-1