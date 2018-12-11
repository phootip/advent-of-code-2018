serial = 9424 % 1000
# serial = 42

grid = [[0 for i in range(300)] for j in range(300)]
def calPower(x,y):
  rackID = x + 10
  power = rackID * y
  power += serial
  power *= rackID
  power %= 1000
  power //= 100
  power -= 5
  return power

def calTotal(x,y):
  power = 0
  for i in range(3):
    for j in range(3):
      power += grid[y+i][x+j]
  return power

for y in range(len(grid)):
  for x in range(len(grid[y])):
    grid[y][x] = calPower(x+1,y+1)
  print('each:',y)

max_power = 0
max_x, max_y = 1, 1
for y in range(len(grid)-2):
  for x in range(len(grid[y])-2):
    total_power = calTotal(x,y)
    if(total_power > max_power):
      max_power = total_power
      max_x = x+1
      max_y = y+1
      print('new max:',max_x,max_y)
  print('total:',y)

print(max_power)
print('x,y:',max_x,max_y)