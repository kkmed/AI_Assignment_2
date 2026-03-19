import random
import heapq

def backtracking(parent, start, goal):
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent[node]

    path.append(start)
    path.reverse()
    return path


def a_star(grid, sx, sy, gx, gy):
    n, m = len(grid), len(grid[0])

    def h(x, y):
        return abs(x - gx) + abs(y - gy)

    pq = [(h(sx, sy), 0, sx, sy)] 
    visited = set()
    parent = {}
    g_score = {(sx, sy): 0}

    while pq:
        f, g, x, y = heapq.heappop(pq)

        if (x, y) == (gx, gy):
            return backtracking(parent, (sx, sy), (gx, gy)), g

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                new_g = g + 1

                if (nx, ny) not in g_score or new_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_g
                    heapq.heappush(pq, (new_g + h(nx, ny), new_g, nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None, -1


N = 70
grid = [[0 for _ in range(N)] for _ in range(N)]

density = float(input("Pick A Density (0.1 / 0.3 / 0.5): "))

for i in range(N):
    for j in range(N):
        if random.random() < density:
            grid[i][j] = 1

sx, sy = map(int, input("Start (x,y): ").split(','))
gx, gy = map(int, input("Goal (x,y): ").split(','))

if grid[sx][sy] == 1 or grid[gx][gy] == 1:
    print("Invalid start/goal (blocked)")
    exit()

path, dist = a_star(grid, sx, sy, gx, gy)

if path:
    print("Shortest Distance:", dist)
    print("Path:", path)
else:
    print("No path exists")