width = 16
height = 26
grid = []
for i in range(0, 416):
    grid.append(0)

for i in range(0, 416, 16):
    print(grid[i//width:i%width*])

for i in range(0, 416):
    y = i//width
    x = i%width
    #print(y, x)