import pygame
import sys
def run(q):
    pygame.init()
    
    writeCells = False

    CELL_SIZE = 10
    ROWS = 100
    COLS = 100
    WINDOW_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    alive_cells = []
    q.append([ROWS, COLS])

    print(q)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Clickable 2D Canvas")
    cell_pos = {}

    def parse_cells():
        for row in range(ROWS):
            for col in range(COLS):
                cell_pos[(row, col)] = 0

    def draw_filled_circle(x, y, radius, color):
        pygame.draw.circle(screen, color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), radius)          



    parse_cells()

    running = True

    while running:
        try:
            alive_cells = q[1]
        except Exception: pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                get_pos()
        screen.fill(WHITE)

        if writeCells :
            for row in range(ROWS):
                for col in range(COLS):
                    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                    
        for cell in range(len(alive_cells)):
            x, y = alive_cells[cell].pos
            draw_filled_circle(x, y, 5, (255,0,0))
        def get_pos():
            x, y = pygame.mouse.get_pos()
            cell_x = x // CELL_SIZE
            cell_y = y // CELL_SIZE
            print(f"Clicked cell at ({cell_x}, {cell_y})")
        pygame.display.flip()
    pygame.quit()
    sys.exit()

