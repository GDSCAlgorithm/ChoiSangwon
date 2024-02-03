import sys
sys.setrecursionlimit(1000000)

def dfs(land, i, j, m, n, check, patch_id):
    if i < 0 or i >= m or j < 0 or j >= n or check[i][j] != 0 or land[i][j] == 0:
        return 0
    check[i][j] = patch_id 
    size = 1  
    
    size += dfs(land, i + 1, j, m, n, check, patch_id)
    size += dfs(land, i - 1, j, m, n, check, patch_id)
    size += dfs(land, i, j + 1, m, n, check, patch_id)
    size += dfs(land, i, j - 1, m, n, check, patch_id)

    return size

def solution(land):
    m = len(land)
    n = len(land[0])
    check = [[0] * n for _ in range(m)]

    patch_sizes = {}
    patch_id = 1

    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and check[i][j] == 0:
                patch_size = dfs(land, i, j, m, n, check, patch_id)
                patch_sizes[patch_id] = patch_size
                patch_id += 1

    max_oil = 0
    for j in range(n):
        oil_in_column = set()
        for i in range(m):
            if check[i][j] != 0:
                oil_in_column.add(check[i][j])

        total_oil = sum(patch_sizes[pid] for pid in oil_in_column)
        max_oil = max(max_oil, total_oil)

    return max_oil