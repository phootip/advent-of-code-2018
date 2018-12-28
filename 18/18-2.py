import pprint

pp = pprint.PrettyPrinter().pprint

f = open('18.txt')
# f = open('18-test.txt')

grid = []
for line in f:
  grid.append([i for i in line.strip()])

maxX = len(grid[0])
maxY = len(grid)
def adj(x,y):
  temp = []
  for y2 in range(-1,2):
    for x2 in range(-1,2):
      if(0 <= x+x2 < maxX and 0 <= y+y2 < maxY and (x2 != 0 or y2 !=0)):
        temp.append(grid[y+y2][x+x2])
  return temp


mem = []
for i in range(10**9):
  # print(i)
  
  # if( i == 37 or i == 37 + 480):
  #   print(i)
  #   wood = 0
  #   lumber = 0
  #   for i in grid:
  #   #   print(''.join(i))
  #     wood += i.count('|')
  #     lumber += i.count('#')
  #   print('wood:',wood)
  #   print('lumber:',lumber)
  #   print('ans:',wood*lumber)
  mem.append(grid)
  next_grid = []
  for y in range(maxY):
    temp = []
    for x in range(maxX):
      adjNodes = adj(x,y)
      if grid[y][x] == '.':
        temp.append('|' if adjNodes.count('|') >= 3 else '.')
      elif grid[y][x] == '|':
        temp.append('#' if adjNodes.count('#') >= 3 else '|')
      else:
        temp.append('#' if adjNodes.count('#') >= 1 and adjNodes.count('|') >= 1 else '.')
    next_grid.append(temp)
  if next_grid in mem:
    # 481
    # if(mem[453] == next_grid):
    #   print(len(mem))
    #   # first mem index = 453
    #   # last mem index = 480
    #   # there is 28 type from 0 to 27
    #   # (10**9 - 453) % 28 + 453
    

    print('Dup!!:',i+1)
    # grid = mem[(10**9 % (len(mem) - mem.index(next_grid))) + mem.index(next_grid)]
    grid = mem[(10**9 - 453) % 28 + 453]
    break
  grid = next_grid

wood = 0
lumber = 0
for i in grid:
#   print(''.join(i))
  wood += i.count('|')
  lumber += i.count('#')

print('wood:',wood)
print('lumber:',lumber)
print('ans:',wood*lumber)