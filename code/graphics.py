import pygame
import sys

def run(q):
    pygame.init()
    
    class IntegerInputField:
        def __init__(self, x, y, width, height):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = (255,255,255)
            self.text = ""
            self.font = pygame.font.Font(None, 36)

        def draw(self, surface):
            pygame.draw.rect(surface, self.color, self.rect)
            text_surface = self.font.render(self.text, True, (0,0,0))
            text_rect = text_surface.get_rect(midleft=self.rect.move(0, 20).topleft)
            surface.blit(text_surface, text_rect)

        def add_digit(self, digit):
            self.text += digit

        def remove_digit(self):
            self.text = self.text[:-1]

        def get_value(self):
            try:
                return int(self.text)
            except ValueError:
                return 0
    class Button:
        def __init__(self, x, y, width, height, text):
            self.rect = pygame.Rect(x, y, width, height)
            self.color = (0,0,0)
            self.text = text
            self.font = pygame.font.Font(None, 36)

        def draw(self, surface):
            pygame.draw.rect(surface, self.color, self.rect)
            text_surface = self.font.render(self.text, True, (255,255,255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    writeCells = False
    paused = False

    CELL_SIZE = 10
    ROWS = 100
    COLS = 150
    #WINDOW_SIZE = (CELL_SIZE * COLS, CELL_SIZE * ROWS)
    WINDOW_SIZE = (1920, 1000)
    clock = pygame.time.Clock()
    FPS = 5

    alive_cells = {}
    q.append([ROWS, COLS])

    input_field = IntegerInputField(1600, 200, 200, 50)
    button = Button(1600, 10, 100, 50, "Pause")
    unpause = Button(960, 500, 100, 50, "Paused")

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("CellSimulator")
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
            alive_cells = q[0]
        except Exception: pass
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button.rect.collidepoint(event.pos) and not paused:
                    paused = True
                elif(unpause.rect.collidepoint(event.pos) and paused):
                    paused = False
                else:
                    get_pos()
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    input_field.add_digit(event.unicode)
                elif event.key == pygame.K_BACKSPACE:
                    input_field.remove_digit()
                
        screen.fill((16, 24, 32))

        if not paused:
            
            if writeCells:
                for row in range(ROWS):
                    for col in range(COLS):
                        pygame.draw.rect(screen, (100,100,100), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            try:
                for cell in alive_cells.keys():
                    x, y = alive_cells[cell].pos
                    draw_filled_circle(x, y, 5, alive_cells[cell].color)
                    alive_cells[cell].think()
            except Exception as e: pass
            def get_pos():
                x, y = pygame.mouse.get_pos()
                cell_x = x // CELL_SIZE
                cell_y = y // CELL_SIZE
                for cell in alive_cells.keys():
                    if(alive_cells[cell].pos == (cell_x, cell_y)):
                        print(f"{alive_cells[cell].pos}, {alive_cells[cell].brain.num_layers}, {alive_cells[cell].color}")

            input_field.draw(screen)
            button.draw(screen)
        if paused:
            pause_font = pygame.font.Font(None, 72)
            unpause.draw(screen)
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()

