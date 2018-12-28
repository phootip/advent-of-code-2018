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

for i in range(10):
  print(i)
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