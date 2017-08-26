def drawPicture(grid):
  # print(len(grid[0]))
  for y in range(len(grid[0])):
    # print(len(grid))
    for x in range(len(grid)):
      print(grid[x][y], end='')
      # print(x,y)
    print('\n')
  
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

drawPicture(grid)
