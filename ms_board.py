import pygame
class Field:
    pass

class Clock_:
    pass


class Board:
    def __init__(self, grid):
        self.window_height, self.window_width, self.window_top, self.block_size = self.set_window(grid)

        pygame.init()
        self.game = pygame.display.set_mode((self.window_width, self.window_height))
        self.game.fill((80, 80, 80))
        draw_grid()

    def set_window(self, grid):
        info = pygame.display.Info()
        width = info.current_w
        height = info.current_h

        block_size = self.set_block_size(grid, width, height)

        window_top = int(((grid[0] * block_size) / 100 * 13) // block_size * block_size)
        window_height = grid[0] * block_size + window_top
        window_width = grid[1] * block_size

        return window_height, window_width, window_top, block_size

    def set_block_size(self, grid, width, height):
        if width < height:
            block_size = round(width // grid[1] * 0.25)
        else:
            block_size = round(height // grid[0] * 0.7)

        return block_size

    def draw_grid(self):
        rect = pygame.Rect(0, 0, self.window_width, self.window_top)
        pygame.draw.rect(game, (140, 140, 140), rect)
        for y in range(self.window_top, self.window_height, self.block_size):
            row = []
            row_visited = []
            for x in range(0, self.window_width, self.block_size):
                row.append(" ")
                row_visited.append(False)
                rect = pygame.Rect(x, y, self.block_size, self.block_size)
                pygame.draw.rect(game, (140, 140, 140), rect, 1)
            field.append(row)
            visited.append(row_visited)
            flags.append(row_visited.copy())


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
            row.append(" ")
            row_visited.append(False)
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(game, black, rect, 1)
        field.append(row)
        visited.append(row_visited)


def draw_field(array):
    for i in range(len(array)):
        print(" ".join(array[i]))


def set_field():
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] != ".":
                if decision(0.15):
                    field[y][x] = "x"
                    set_numbers(x, y)


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


def counter(y, x):
    piece = field[y][x]
    if piece != "x":
        if piece in (" ", "."):
            piece = "0"
        field[y][x] = str(int(piece) + 1)


def set_blocks_around(x, y, string):
    x = x // block_size
    y = y // block_size

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
    x_pix = x * block_size
    y_pix = y * block_size

    draw_rect(x_pix, y_pix, black)

    if field[y][x] in [" ", "."] and visited[y][x] is False:
        visited[y][x] = True
        free_field(x, y)

    draw_numbers(x_pix, y_pix)


def draw_numbers(x, y):
    x = x // block_size
    y = y // block_size
    if field[y][x] not in (".", "x", " "):
        visited[y][x] = True
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(str(field[y][x]), False, colors[int(field[y][x])])
        if font_size % 2 == 0:
            i = 0
        else:
            i = 1
        game.blit(text, (x * block_size + (font_size // 2 - i), y * block_size))
