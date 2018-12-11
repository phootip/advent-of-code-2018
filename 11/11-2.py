serial = 9424 % 1000
# serial = 42

grid = [[0 for i in range(300)] for j in range(300)]
mem = [[[99 for i in range(300)] for j in range(300)] for k in range(300)]
def calPower(x,y):
  rackID = x + 10
  power = rackID * y
  power += serial
  power *= rackID
  power %= 1000
  power //= 100
  power -= 5
  return power

def calTotal(x,y,size):
  if(mem[size][y][x] != 99):
    return mem[size][y][x]
  if(x < 0 or y < 0 or x > 299 or y > 299 or size > 299):
    return 0
  if(size == 0):
    mem[size][y][x] = grid[y][x]
    return mem[size][y][x]
  
  result = calTotal(x,y,size-1)
  for i in range(size+1):
    result += grid[y+size-i][x+size]
  for i in range(size+1):
    result += grid[y+size][x+size-i]
  result -= grid[y+size][x+size]
  mem[size][y][x] = result
  return mem[size][y][x]

for y in range(len(grid)):
  for x in range(len(grid[y])):
    grid[y][x] = calPower(x+1,y+1)
  print('each:',y)

max_power = 0
max_x, max_y, max_size = 1, 1, 0
for y in range(len(grid)):
  for x in range(len(grid[y])):
    edge = max(x,y)
    for size in range(300-edge):
      c_power = calTotal(x,y,size)
      if(c_power > max_power):
        max_power = c_power
        max_x = x + 1
        max_y = y + 1
        max_size = size + 1
        print('new_max:',max_power)
  print(y)
  
print(max_power)
print('x,y,size:',max_x,max_y,max_size)