import random
import heapq
import copy

N = 70

def update_dynamic_obstacles(grid, change_prob=0.001):
    for i in range(N):
        for j in range(N):
            if random.random() < change_prob:
                grid[i][j] = 1 - grid[i][j]

def backtracking(parent, start, goal):
    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    return path

def a_star(grid, sx, sy, gx, gy):
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

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                new_g = g + 1

                if (nx, ny) not in g_score or new_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = new_g
                    heapq.heappush(pq, (new_g + h(nx, ny), new_g, nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None, -1


grid = [[0 for _ in range(N)] for _ in range(N)]
actual_grid = copy.deepcopy(grid)
known_grid = [[0 for _ in range(N)] for _ in range(N)]

density = float(input("Pick A Density (0.1/0.3/0.5): "))

# generate obstacles
for i in range(N):
    for j in range(N):
        if random.random() < density:
            actual_grid[i][j] = 1

sx, sy = map(int, input("Start (x,y): ").split(','))
gx, gy = map(int, input("Goal (x,y): ").split(','))

# ensure start and goal are free
if actual_grid[sx][sy] == 1 or actual_grid[gx][gy] == 1:
    print("Invalid start/goal")
    exit()

current = (sx, sy)
trajectory = [current]

replans = 0
max_steps = 10000  
steps = 0

while current != (gx, gy) and steps < max_steps:

    path, _ = a_star(known_grid, current[0], current[1], gx, gy)

    if not path:
        replans += 1
        update_dynamic_obstacles(actual_grid)
        continue

    next_step = path[1]

    update_dynamic_obstacles(actual_grid)

    if actual_grid[next_step[0]][next_step[1]] == 1:
        known_grid[next_step[0]][next_step[1]] = 1
        replans += 1
        continue

    current = next_step
    trajectory.append(current)

    x, y = current
    known_grid[x][y] = actual_grid[x][y]

    for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            known_grid[nx][ny] = actual_grid[nx][ny]

    steps += 1

print("\nTrajectory:", trajectory)
print("Steps:", len(trajectory) - 1)
print("Replans:", replans)

if current == (gx, gy):
    print("Status: Reached Goal")
else:
    print("Status: Failed")