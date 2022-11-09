#click
#freespace
#bombs generated + numbers +=
#set all fields without any bomb and number free
#start clicking
#clicked -> on number, free space, bomb
#   number:         print number
#   free space:     reveal evertyhing next to space
#   bomb:           you lost -> lose screen / restart

#
#import pygame
#pygame.init()
#info = pygame.display.Info()
#
#width = info.current_w
#height = info.current_h
#
#grid = (26, 16)
#
#if width < height:
#    block_size = round(width // grid[1] * 0.30)
#else:
#    block_size = round(height // grid[0] * 0.75)
#
#window_width = grid[1] * block_size
#window_height = grid[0] * block_size + (grid[0] * block_size) / 100 * 13
#
#
#print("\n\nHeight: ", height, "\nWidth: ", width, sep="")
#print("\nBlock Size: ", block_size, sep="")
#print("Window Height: ", window_height, "\nWindow Width: ", window_width, sep="")
#
#

gray = (203,203,203)
black = (140, 140, 140)
block_size = 32
grid = (24, 15)
font_size = round(block_size * 0.83)

window_height = 0#grid[0] * block_size
window_width = 0#grid[1] * block_size
screen_height = 1080
screen_width = 1920
