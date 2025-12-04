from collections import deque

DIRS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def read_grid(path="input.txt"):
    with open(path, "r") as f:
        grid = [list(line.rstrip("\n")) for line in f]
    return grid

def count_removed_iteratively(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows>0 else 0

    neighbor_counts = [[0]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            cnt = 0
            for dr,dc in DIRS:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    cnt += 1
            neighbor_counts[r][c] = cnt

    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and neighbor_counts[r][c] < 4:
                q.append((r,c))

    removed = 0

    while q:
        r,c = q.popleft()

        if grid[r][c] != '@':
            continue

        if neighbor_counts[r][c] >= 4:
            continue

        grid[r][c] = '.'
        removed += 1

        for dr, dc in DIRS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                neighbor_counts[nr][nc] -= 1
                if neighbor_counts[nr][nc] < 4:
                    q.append((nr,nc))

    return removed

grid = read_grid("input.txt")
total_removed = count_removed_iteratively(grid)
print("Total rolls removed:", total_removed)
