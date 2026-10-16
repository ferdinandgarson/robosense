import heapq

def h(a, b):  # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(h(start, goal), 0, start)]
    came_from, cost = {}, {start: 0}
    while open_list:
        _, g, cur = heapq.heappop(open_list)
        if cur == goal:
            path = [cur]
            while cur in came_from:
                cur = came_from[cur]
                path.append(cur)
            return path[::-1]
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            n = (cur[0]+dr, cur[1]+dc)
            if 0 <= n[0] < rows and 0 <= n[1] < cols and grid[n[0]][n[1]] == 0:
                if g + 1 < cost.get(n, 10**9):
                    cost[n] = g + 1
                    came_from[n] = cur
                    heapq.heappush(open_list, (g + 1 + h(n, goal), g + 1, n))
    return None  # no path

if __name__ == "__main__":
    from environment import make_grid
    print(astar(make_grid(), (0,0), (5,5)))