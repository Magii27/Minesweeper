import pygame

gray = (203,203,203)
black = (140, 140, 140)
block_size = 30
grid = (24, 15)
font_size = round(block_size * 0.83)

window_height = grid[0] * block_size
window_width = grid[1] * block_size
screen_height = 1080
screen_width = 1920


colors = {1:(0, 102, 204), 2:(0, 153, 0), 3:(255, 51, 51), 4:(0, 0, 204), 5:(153, 0, 0), 6:(0, 204, 204), 7:(0, 0, 0), 8:(96, 96, 96)}


def main():
    global game, CLOCK, gray, font_size, colors, visited, restart, field
    pygame.init()
    game = pygame.display.set_mode((window_width, window_height))
    CLOCK = pygame.time.Clock()
    game.fill((80,80, 80))
    field = []
    visited = []
    drawGrid()
    first_click = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x_array = x // block_size
                y_array = y // block_size

                if pygame.mouse.get_pressed()[0]:
                    if first_click:
                        set_blocks_around(x, y, ".")
                        set_field()
                        draw_field(field)
                        first_click = False

                    if field[y_array][x_array] in [".", " "]:
                        draw_rect(x, y, black)
                        free_field(x_array, y_array)
                    elif field[y_array][x_array] == "x":
                        restart = True
                        draw_rect(x, y, black)
                        draw_numbers(x, y)
                        pygame.quit()
                        return
                    else:
                        draw_rect(x, y, black)
                        draw_numbers(x, y)

                if pygame.mouse.get_pressed()[2]:
                    if visited[y_array][x_array] is False:
                        draw_rect(x, y, (255, 0, 0))

            if event.type == pygame.QUIT:
                restart = False
                pygame.quit()
                sys.exit()

        pygame.display.update()