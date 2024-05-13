from collections import deque

def init_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = ['0'] * cols
        matrix.append(row)

    matrix[0][0] = 'A'
    matrix[4][0] = 'B'

    matrix[0][3] = '1'
    matrix[1][1] = '1'
    matrix[2][1] = '1'
    matrix[3][4] = '1'
    matrix[3][5] = '1'
    matrix[4][4] = '1'
    matrix[5][4] = '1'
    matrix[5][3] = '1'
    matrix[5][5] = '1'

    return matrix

def display(matrix):    
    for r in matrix:
        print(r)

def exist_path(matrix, START, END):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    path = []
    def dfs(r, c):
        visited.add((r, c))
        path.append((r, c))
        if matrix[r][c] == END:
            return True

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != '1' and (nr, nc) not in visited:
                has_path = dfs(nr, nc)
                if has_path:
                    return True

        return False

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == START:
                has_path = dfs(r, c) 
                if has_path: return True, path
            
    return False, path

def has_path(matrix, START, END):
    rows, cols = len(matrix), len(matrix[0])
    def bfs(r, c):
        visited = set()
        queue = deque({(0, 0, 0, [])})
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue:
            r, c, length, path = queue.popleft()
            path.append((r, c))
            if matrix[r][c] == END:
                return True, length, path
            
            for i, j in directions:
                nr, nc = r + i, c +j
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != '1' and (nr, nc) not in visited:
                    queue.append((nr, nc, length + 1, path))
                    visited.add((nr, nc))
        return False, 0, []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == START:
                has_path, length, path = bfs(r, c) 
                if has_path: return True, length, path

    return False, 0, []



if __name__ == "__main__":
    matrix = init_matrix(6, 6)
    # matrix[0][1] = '1'
    matrix[1][0] = '1'
    # matrix[3][1] = '1'
    # matrix[4][1] = '1'
    # matrix[5][1] = '1'
    display(matrix)
    # has_path, path = exist_path(matrix, 'A', 'B')
    # print(has_path)
    # print(path)
    has_path, path, length = has_path(matrix, 'A', 'B')
    print(has_path)
    print(length)
    print(path)

