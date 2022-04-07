import sys
import pygame


gray = (203,203,203)
black = (140, 140, 140)
block_size = 30
grid = (26, 16)

window_height = grid[0] * block_size
window_width = grid[1] * block_size
screen_height = 1080
screen_width = 1920

field = []

def main():
    global game, CLOCK, gray
    pygame.init()
    game = pygame.display.set_mode((window_width, window_height))
    CLOCK = pygame.time.Clock()
    game.fill(black)
    drawGrid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:

                    x, y = pygame.mouse.get_pos()
                    print(x // block_size * block_size // block_size, y // block_size * block_size // block_size)
                    draw_rect(x, y, (80,80, 80))

                if pygame.mouse.get_pressed()[2]:
                    x, y = pygame.mouse.get_pos()
                    draw_rect(x, y, (255, 0, 0))

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def get_block_position(x, y):
    x = x // block_size * block_size
    y = y // block_size * block_size

    return x, y


def draw_rect(x, y, RGB):
    position = get_block_position(x, y)
    rect = pygame.Rect(position[0], position[1], block_size, block_size)
    pygame.draw.rect(game, RGB, rect)
    pygame.draw.rect(game, black, rect, 1)



def drawGrid():
    global block_size, field
    field = []
    for x in range(0, window_width, block_size):
        row = []
        for y in range(0, window_height, block_size):
            row.append(str(x//block_size) + "-" + str(y//block_size))
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(game, gray, rect, 1)
        field.append(row)
    print(field)

main()