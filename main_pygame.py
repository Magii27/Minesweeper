import sys
import pygame
import random


gray = (203,203,203)
black = (140, 140, 140)
block_size = 45
grid = (26, 16)
font_size = round(block_size * 0.83)

window_height = grid[0] * block_size
window_width = grid[1] * block_size
screen_height = 1080
screen_width = 1920

field = []
visited = []
colors = {1:(0, 102, 204), 2:(0, 153, 0), 3:(255, 51, 51), 4:(0, 0, 204), 5:(153, 0, 0), 6:(0, 204, 204), 7:(0, 0, 0), 8:(96, 96, 96)}
count = 0


def main():
    global game, CLOCK, gray, count, font_size, colors, visited
    pygame.init()
    game = pygame.display.set_mode((window_width, window_height))
    CLOCK = pygame.time.Clock()
    game.fill((80,80, 80))
    drawGrid()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    x_array = x // block_size
                    y_array = y // block_size
                    if count == 0:
                        set_blocks_around(x, y, ".")
                        set_field()
                        count += 1
                        print(len(field[0]), len(field))
                        draw_field(field)

                    if field[y_array][x_array] in [".", " "]:
                        #alles nebenan aufdecken
                        draw_rect(x, y, black)
                        free_field(x_array, y_array)
                        #draw_numbers(x, y)
                    elif field[y_array][x_array] == "x":
                        draw_rect(x, y, black)
                        draw_numbers(x, y)

                    else:
                        #nummer aufdecken
                        draw_rect(x, y, black)
                        draw_numbers(x, y)


                    #print(x // block_size * block_size // block_size, y // block_size * block_size // block_size)


                if pygame.mouse.get_pressed()[2]:
                    x, y = pygame.mouse.get_pos()
                    draw_rect(x, y, (255, 0, 0))

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def free_field(x, y):
    if y == 0:
        if x == 0:
            #set_free(y, x)
            set_free(y + 1, x)
            set_free(y, x + 1)
            set_free(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            #set_free(y, x)
            set_free(y + 1, x)
            set_free(y, x - 1)
            set_free(y + 1, x - 1)
        else:
            #set_free(y, x)
            set_free(y, x - 1)
            set_free(y, x + 1)
            set_free(y + 1, x)
            set_free(y + 1, x - 1)
            set_free(y + 1, x - 1)
    elif y == len(field) - 1:
        if x == 0:
            #set_free(y, x)
            set_free(y - 1, x)
            set_free(y, x + 1)
            set_free(y - 1, x + 1)
        elif x == len(field[0]) - 1:
            #set_free(y, x)
            set_free(y - 1, x)
            set_free(y, x - 1)
            set_free(y - 1, x - 1)
        else:
            #set_free(y, x)
            set_free(y, x - 1)
            set_free(y, x + 1)
            set_free(y - 1, x)
            set_free(y - 1, x - 1)
            set_free(y - 1, x + 1)
    else:
        if x == 0:
            #set_free(y, x)
            set_free(y - 1, x)
            set_free(y + 1, x)
            set_free(y, x + 1)
            set_free(y - 1, x + 1)
            set_free(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            #set_free(y, x)
            set_free(y - 1, x)
            set_free(y + 1, x)
            set_free(y, x - 1)
            set_free(y - 1, x - 1)
            set_free(y + 1, x - 1)
        else:
            #set_free(y, x)
            set_free(y, x - 1)
            set_free(y, x + 1)
            set_free(y - 1, x)
            set_free(y - 1, x - 1)
            set_free(y - 1, x + 1)
            set_free(y + 1, x)
            set_free(y + 1, x - 1)
            set_free(y + 1, x + 1)
    pass


def set_free(y, x):
    x_pix = x * block_size
    y_pix = y * block_size

    draw_rect(x_pix, y_pix, black)

    if field[y][x] in [" ", "."] and visited[y][x] is False:
        #print(field[y][x])
        visited[y][x] = True
        free_field(x, y)

    draw_numbers(x_pix, y_pix)



def set_blocks_around(x, y, string):
    x = x // block_size
    y = y // block_size
    print(x, y)

    if y == 0:
        if x == 0:
            field[y][x] = string
            field[y + 1][x] = string
            field[y][x + 1] = string
            field[y + 1][x + 1] = string
        elif x == len(field[0]) - 1:
            field[y][x] = string
            field[y + 1][x] = string
            field[y][x - 1] = string
            field[y + 1][x - 1] = string
        else:
            field[y][x] = string
            field[y][x - 1] = string
            field[y][x + 1] = string
            field[y + 1][x] = string
            field[y + 1][x - 1] = string
            field[y + 1][x + 1] = string
    elif y == len(field) - 1:
        if x == 0:
            field[y][x] = string
            field[y - 1][x] = string
            field[y][x + 1] = string
            field[y - 1][x + 1] = string
        elif x == len(field[0]) - 1:
            field[y][x] = string
            field[y - 1][x] = string
            field[y][x - 1] = string
            field[y - 1][x - 1] = string
        else:
            field[y][x] = string
            field[y][x - 1] = string
            field[y][x + 1] = string
            field[y - 1][x] = string
            field[y - 1][x - 1] = string
            field[y - 1][x + 1] = string
    else:
        if x == 0:
            field[y][x] = string
            field[y - 1][x] = string
            field[y + 1][x] = string
            field[y][x + 1] = string
            field[y - 1][x + 1] = string
            field[y + 1][x + 1] = string
        elif x == len(field[0]) - 1:
            field[y][x] = string
            field[y - 1][x] = string
            field[y + 1][x] = string
            field[y][x - 1] = string
            field[y - 1][x - 1] = string
            field[y + 1][x - 1] = string
        else:
            field[y][x] = string
            field[y][x - 1] = string
            field[y][x + 1] = string
            field[y - 1][x] = string
            field[y - 1][x - 1] = string
            field[y - 1][x + 1] = string
            field[y + 1][x] = string
            field[y + 1][x - 1] = string
            field[y + 1][x + 1] = string


def counter(y, x):
    piece = field[y][x]
    if piece != "x":
        if piece in (" ", "."):
            piece = "0"
        field[y][x] = str(int(piece) + 1)


def draw_numbers(x, y):
    x = x // block_size
    y = y // block_size
    if field[y][x] not in (".", "x", " "):
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(str(field[y][x]), False, colors[int(field[y][x])])
        # text = pygame.transform.smoothscale(text.convert(), ())
        if font_size % 2 == 0:
            i = 0
        else:
            i = 1
        game.blit(text, (x * block_size + (font_size//2 - i), y * block_size))


def set_numbers(x, y):
    #x = x // block_size
    #y = y // block_size

    if y == 0:
        if x == 0:
            counter(y, x)
            counter(y + 1, x)
            counter(y, x + 1)
            counter(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            counter(y, x)
            counter(y + 1, x)
            counter(y, x - 1)
            counter(y + 1, x - 1)
        else:
            counter(y, x)
            counter(y, x - 1)
            counter(y, x + 1)
            counter(y + 1, x)
            counter(y + 1, x - 1)
            counter(y + 1, x - 1)
    elif y == len(field) - 1:
        if x == 0:
            counter(y, x)
            counter(y - 1, x)
            counter(y, x + 1)
            counter(y - 1, x + 1)
        elif x == len(field[0]) - 1:
            counter(y, x)
            counter(y - 1, x)
            counter(y, x - 1)
            counter(y - 1, x - 1)
        else:
            counter(y, x)
            counter(y, x - 1)
            counter(y, x + 1)
            counter(y - 1, x)
            counter(y - 1, x - 1)
            counter(y - 1, x + 1)
    else:
        if x == 0:
            counter(y, x)
            counter(y - 1, x)
            counter(y + 1, x)
            counter(y, x + 1)
            counter(y - 1, x + 1)
            counter(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            counter(y, x)
            counter(y - 1, x)
            counter(y + 1, x)
            counter(y, x - 1)
            counter(y - 1, x - 1)
            counter(y + 1, x - 1)
        else:
            counter(y, x)
            counter(y, x - 1)
            counter(y, x + 1)
            counter(y - 1, x)
            counter(y - 1, x - 1)
            counter(y - 1, x + 1)
            counter(y + 1, x)
            counter(y + 1, x - 1)
            counter(y + 1, x + 1)


def decision(probability):
    return random.random() < probability


def draw_field(array):
    for i in range(len(array)):
        print(" ".join(array[i]))


def set_field():
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] != ".":
                if decision(0.15):
                    #set_blocks_around(x, y, "x")
                    field[y][x] = "x"
                    set_numbers(x, y)


def get_block_position(x, y):
    x = x // block_size * block_size
    y = y // block_size * block_size

    return x, y


def draw_rect(x, y, RGB):
    position = get_block_position(x, y)
    rect = pygame.Rect(position[0], position[1], block_size, block_size)
    pygame.draw.rect(game, RGB, rect)
    pygame.draw.rect(game, gray, rect, 1)



def drawGrid():
    global block_size, field, game
    field = []
    for y in range(0, window_height, block_size):
        row = []
        row_visited = []
        for x in range(0, window_width, block_size):
            #row.append(str(x//block_size) + "-" + str(y//block_size))
            row.append(" ")
            row_visited.append(False)
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(game, black, rect, 1)
        field.append(row)
        visited.append(row_visited)
    print(field)

main()