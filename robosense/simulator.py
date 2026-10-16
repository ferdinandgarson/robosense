import pygame
from environment import make_grid, SIZE
from astar import astar

CELL = 30
pygame.init()
screen = pygame.display.set_mode((SIZE*CELL, SIZE*CELL))
clock = pygame.time.Clock()

grid = make_grid()
robot, goal, path = (0, 0), (19, 19), []

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            c, r = e.pos[0]//CELL, e.pos[1]//CELL
            grid[r][c] = 1 - grid[r][c]
            if path:  # new obstacle: re-plan
                path = astar(grid, robot, goal) or []
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            path = astar(grid, robot, goal) or []

    if len(path) > 1:
        path.pop(0)
        robot = path[0]

    screen.fill((255, 255, 255))
    for r in range(SIZE):
        for c in range(SIZE):
            rect = (c*CELL, r*CELL, CELL, CELL)
            if grid[r][c]: pygame.draw.rect(screen, (40, 40, 40), rect)
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)
    pygame.draw.rect(screen, (0, 200, 0), (goal[1]*CELL, goal[0]*CELL, CELL, CELL))
    pygame.draw.circle(screen, (220, 40, 40), (robot[1]*CELL+CELL//2, robot[0]*CELL+CELL//2), CELL//3)
    pygame.display.flip()
    clock.tick(8)
pygame.quit()