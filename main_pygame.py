import sys
import pygame
import random
from threading import Thread
import threading
from time import sleep

gray = (203,203,203)
black = (140, 140, 140)
block_size = 32
grid = (24, 15)
font_size = round(block_size * 0.83)

#window_height = 0#grid[0] * block_size
#window_width = 0#grid[1] * block_size

colors = {1:(0, 102, 204), 2:(0, 153, 0), 3:(255, 51, 51), 4:(0, 0, 204), 5:(153, 0, 0), 6:(0, 204, 204), 7:(0, 0, 0), 8:(96, 96, 96)}


def main():
    global game, gray, font_size, colors, visited, restart, field, flags, block_size, font_size, window_height, window_width, window_top, t_id
    pygame.init()
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h

    if width < height:
        block_size = round(width // grid[1] * 0.25)
    else:
        block_size = round(height // grid[0] * 0.7)

    window_top = int(((grid[0] * block_size) / 100 * 13) // block_size * block_size)
    window_height = grid[0] * block_size + window_top

    window_width = grid[1] * block_size
    font_size = round(block_size * 0.83)
    game = pygame.display.set_mode((window_width, window_height))
    CLOCK = pygame.time.Clock()

    game.fill((80,80, 80))
    field = []
    visited = []
    flags = []
    drawGrid()
    first_click = True
    draw_rect(round(window_width / 6), round(window_top / 3), (round(window_width / 6), round(window_top / 3)),
              (0, 0, 0), (0, 0, 0))
    font = pygame.font.SysFont("Arial", font_size)

    text = font.render("00:00", False, (255, 255, 255))
    game.blit(text, (round(window_width / 6), round(window_top / 3)))
    while True:

        if not first_click:
            counting_time = pygame.time.get_ticks() - start_time
            CLOCK.tick(60)

            counting_minutes = str(counting_time // 60000).zfill(2)
            counting_seconds = str((counting_time % 60000) // 1000).zfill(2)
            counting_millisecond = str(counting_time % 1000).zfill(3)
#
            counting_string = "%s:%s" % (counting_minutes, counting_seconds)
            font = pygame.font.SysFont("Arial", font_size)
            draw_rect(round(window_width / 6), round(window_top / 3), (round(window_width / 6), round(window_top / 3)),
                      (0, 0, 0), (0, 0, 0))

            text = font.render(str(counting_string), False, (255, 255, 255))
            game.blit(text, (round(window_width/6), round(window_top/3)))


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if y <= window_top:
                    continue

                pos_ary = get_coordinates_array(x, y)
                pos_pix = get_coordinates_field(pos_ary[0], pos_ary[1])
                if pygame.mouse.get_pressed()[0]:
                    if first_click:
                        start_time = pygame.time.get_ticks()
                        set_blocks_around(pos_pix[0], pos_pix[1], ".")
                        set_field()
                        draw_field(field)
                        counting_time = pygame.time.get_ticks() - start_time

                        # change milliseconds into minutes, seconds, milliseconds
                        counting_minutes = str(counting_time // 60000).zfill(2)
                        counting_seconds = str((counting_time % 60000) // 1000).zfill(2)
                        counting_millisecond = str(counting_time % 1000).zfill(3)
                        #
                        counting_string = "%s:%s" % (counting_minutes, counting_seconds)

                        draw_rect(round(window_width / 6), round(window_top / 3),
                                  (round(window_width / 6), round(window_top / 3)), (0, 0, 0), (0, 0, 0))
                        # print(counting_string)
                        font = pygame.font.SysFont("Arial", font_size)
                        # counting_text = font.render(str(counting_string), 1, (0, 0, 0))
                        text = font.render(str(counting_string), False, (255, 255, 255))
                        game.blit(text, (round(window_width / 6), round(window_top / 3)))
                        first_click = False

                    if flags[pos_ary[1]][pos_ary[0]] is True:
                        pass
                    elif field[pos_ary[1]][pos_ary[0]] in [".", " "]:
                        draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size), black, gray)
                        free_field(pos_ary[0], pos_ary[1])
                    elif field[pos_ary[1]][pos_ary[0]] == "x":
                        restart = True
                        draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size),  black, gray)
                        draw_numbers(pos_pix[0], pos_pix[1])
                        pygame.quit()
                        return
                    else:
                        draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size), black, gray)
                        draw_numbers(pos_pix[0], pos_pix[1])

                if pygame.mouse.get_pressed()[2]:
                    if visited[pos_ary[1]][pos_ary[0]] is False:
                        if flags[pos_ary[1]][pos_ary[0]] is False:
                            draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size), (255, 0, 0), gray)
                            flags[pos_ary[1]][pos_ary[0]] = True
                        else:
                            draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size), (80,80, 80), gray)
                            flags[pos_ary[1]][pos_ary[0]] = False

            if event.type == pygame.QUIT:
                restart = False
                pygame.quit()
                sys.exit()

        pygame.display.update()


def get_coordinates_array(x, y):
    x = (x) // block_size
    y = (y - window_top) // block_size

    return x, y


def get_coordinates_field(x, y):
    x = x * block_size
    y = y * block_size + window_top

    return x, y


def free_field(x, y):
    if y == 0:
        if x == 0:
            set_free(y, x)
            set_free(y + 1, x)
            set_free(y, x + 1)
            set_free(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            set_free(y, x)
            set_free(y + 1, x)
            set_free(y, x - 1)
            set_free(y + 1, x - 1)
        else:
            set_free(y, x)
            set_free(y, x - 1)
            set_free(y, x + 1)
            set_free(y + 1, x)
            set_free(y + 1, x - 1)
            set_free(y + 1, x - 1)
    elif y == len(field) - 1:
        if x == 0:
            set_free(y, x)
            set_free(y - 1, x)
            set_free(y, x + 1)
            set_free(y - 1, x + 1)
        elif x == len(field[0]) - 1:
            set_free(y, x)
            set_free(y - 1, x)
            set_free(y, x - 1)
            set_free(y - 1, x - 1)
        else:
            set_free(y, x)
            set_free(y, x - 1)
            set_free(y, x + 1)
            set_free(y - 1, x)
            set_free(y - 1, x - 1)
            set_free(y - 1, x + 1)
    else:
        if x == 0:
            set_free(y, x)
            set_free(y - 1, x)
            set_free(y + 1, x)
            set_free(y, x + 1)
            set_free(y - 1, x + 1)
            set_free(y + 1, x + 1)
        elif x == len(field[0]) - 1:
            set_free(y, x)
            set_free(y - 1, x)
            set_free(y + 1, x)
            set_free(y, x - 1)
            set_free(y - 1, x - 1)
            set_free(y + 1, x - 1)
        else:
            set_free(y, x)
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
    pos_pix = get_coordinates_field(x, y)

    if field[y][x] != "x":
        draw_rect(pos_pix[0], pos_pix[1], (block_size, block_size), black, gray)

    if field[y][x] in [" ", "."] and visited[y][x] is False:
        visited[y][x] = True
        free_field(x, y)

    draw_numbers(pos_pix[0], pos_pix[1])


def set_blocks_around(x, y, string):
    pos_ary = get_coordinates_array(x, y)

    if y == 0:
        if x == 0:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] + 1][pos_ary[0] + 1] = string
        elif pos_ary[0] == len(field[0]) - 1:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1] + 1][pos_ary[0] - 1] = string
        else:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0] - 1] = string
            field[pos_ary[1] + 1][pos_ary[0] + 1] = string
    elif pos_ary[1] == len(field) - 1:
        if pos_ary[0] == 0:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] - 1][pos_ary[0] + 1] = string
        elif pos_ary[0] == len(field[0]) - 1:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1] - 1][pos_ary[0] - 1] = string
        else:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0] - 1] = string
            field[pos_ary[1] - 1][pos_ary[0] + 1] = string
    else:
        if pos_ary[0] == 0:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] - 1][pos_ary[0] + 1] = string
            field[pos_ary[1] + 1][pos_ary[0] + 1] = string
        elif pos_ary[0] == len(field[0]) - 1:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1] - 1][pos_ary[0] - 1] = string
            field[pos_ary[1] + 1][pos_ary[0] - 1] = string
        else:
            field[pos_ary[1]][pos_ary[0]] = string
            field[pos_ary[1]][pos_ary[0] - 1] = string
            field[pos_ary[1]][pos_ary[0] + 1] = string
            field[pos_ary[1] - 1][pos_ary[0]] = string
            field[pos_ary[1] - 1][pos_ary[0] - 1] = string
            field[pos_ary[1] - 1][pos_ary[0] + 1] = string
            field[pos_ary[1] + 1][pos_ary[0]] = string
            field[pos_ary[1] + 1][pos_ary[0] - 1] = string
            field[pos_ary[1] + 1][pos_ary[0] + 1] = string


def counter(y, x):
    piece = field[y][x]
    if piece != "x":
        if piece in (" ", "."):
            piece = "0"
        field[y][x] = str(int(piece) + 1)


def draw_numbers(x, y):

    pos_ary = get_coordinates_array(x, y)
    pos_pix = get_coordinates_field(pos_ary[0], pos_ary[1])
    if field[pos_ary[1]][pos_ary[0]] not in (".", "x", " "):
        visited[pos_ary[1]][pos_ary[0]] = True
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(str(field[pos_ary[1]][pos_ary[0]]), False, colors[int(field[pos_ary[1]][pos_ary[0]])])
        if font_size % 2 == 0:
            i = 0
        else:
            i = 1
        game.blit(text, (pos_pix[0] + (font_size//2 - i), pos_pix[1]))


def set_numbers(x, y):
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
            counter(y + 1, x + 1)
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
    print()


def set_field():
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] != ".":
                if decision(0.15):
                    field[y][x] = "x"
                    set_numbers(x, y)


def draw_rect(x, y, size, RGB_rect, RGB_frame):
    pos_ary = get_coordinates_array(x, y)
    pos_pix = get_coordinates_field(pos_ary[0], pos_ary[1])
    rect = pygame.Rect(pos_pix[0], pos_pix[1], size[0], size[1])
    pygame.draw.rect(game, RGB_rect, rect)
    #pygame.draw.rect(game, gray, rect, 1)
    draw_rect_frame(rect, RGB_frame)


def draw_rect_frame(rect, RGB):
    pygame.draw.rect(game, RGB, rect, 1)


def drawGrid():
    global block_size, field, game, flags
    field = []
    rect = pygame.Rect(0,0, window_width, window_top)
    pygame.draw.rect(game, black, rect)
    for y in range(window_top, window_height, block_size):
        row = []
        row_visited = []
        for x in range(0, window_width, block_size):
            row.append(" ")
            row_visited.append(False)
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(game, black, rect, 1)
        field.append(row)
        visited.append(row_visited)
        flags.append(row_visited.copy())


restart = True

while True:
    if restart:
        main()
    else:
        break
