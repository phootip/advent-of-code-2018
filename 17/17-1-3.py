from PIL import Image, ImageDraw

# f = open('./17/17.txt')
f = open('./17.txt')
# f = open('17-test.txt')

nodes = [(500,0)]
revisit = []
maps = [['.' for i in range(2000)] for j in range(2000)]
for line in f:
  line = line.strip().split(',')
  line = list(map(lambda x: x.strip().split('='),line))
  line[1][1] = list(map(int,line[1][1].split('..')))
  line[0][1] = int(line[0][1])
  p1 = line[0][1]
  p21 = line[1][1][0]
  p22 = line[1][1][1]
  if line[0][0] == 'x': 
    for i in range(p21,p22+1):
      maps[i][p1] = '#'
  else:
    for i in range(p21,p22+1):
      maps[p1][i] = '#'

maps[0][500] = '|'

minX, maxX = 2100,0
minY, maxY = 2100,0
for y in range(2000):
  for x in range(2000):
    if maps[y][x] != '.':
      minX = min(minX,x)
      maxX = max(maxX,x)
      minY = min(minY,y)
      maxY = max(maxY,y)

def draw():
  ans = 0
  im = Image.new('RGB', (2000, 2000), color = 'white')
  draw = ImageDraw.Draw(im)
  for y in range(minY+1,maxY+1):
    for x in range(minX-1,maxX+2):
      # print(maps[y][x],end='')
      if(maps[y][x] == '|'):
        draw.rectangle([(x,y),(x,y)],fill='green')
        ans += 1
      elif(maps[y][x] == '#'):
        draw.rectangle([(x,y),(x,y)],fill='brown')
        ans += 0
      elif(maps[y][x] == '~'):
        draw.rectangle([(x,y),(x,y)],fill='blue')
        ans += 1
    # print()
  # im = im.crop((450,0,550,100))
  # im = im.resize((500,500))
  im.save(f"./visual/ans.png")
  return ans

def deadEnd(x,y,d):
  if(maps[y][x] == '|' and (maps[y+1][x] == '#' or maps[y+1][x] == '~')):
    return deadEnd(x+d,y,d)
  if(maps[y][x] == '#'):
    return True
  elif(maps[y][x] == '.'):
    maps[y][x] = '|'
    if(maps[y+1][x] == '#' or maps[y+1][x] == '~'):
      return deadEnd(x+d,y,d)
    elif(maps[y+1][x] == '.'):
      nodes.append((x,y+1))
      revisit.append((x,y))
      maps[y+1][x] = '|'
      return False
  return False

def still(x,y,d):
  while(maps[y][x] == '|'):
    maps[y][x] = '~'
    if(maps[y-1][x] == '|'):
      nodes.append((x,y-1))
    x += d

def check(x,y,d):
  if(maps[y][x] == '|'):
    return check(x+d,y,d)
  if(maps[y][x] == '.'):
    return False
  if(maps[y][x] == '#'):
    return True

def cycle():
  while nodes:
    x,y = nodes.pop(0)
    if(y > maxY):
      continue
    if(maps[y+1][x] == '.'):
      nodes.append((x,y+1))
      maps[y+1][x] = '|'
    elif(maps[y+1][x] == '#' or maps[y+1][x] == '~'):
      right = deadEnd(x+1,y,1)
      left = deadEnd(x-1,y,-1)
      if right and left:
        still(x,y,1)
        still(x-1,y,-1)
  return True

while nodes:
  temp = revisit[:]
  cycle()
  for x,y in revisit:
    right = check(x+1,y,1)
    left = check(x-1,y,-1)
    if( right and left ):
      still(x,y,1)
      still(x-1,y,-1)
  
  
  
ans = draw()

print(minX,minY)
print(maxX,maxY)
print(ans)

# print(ans - 1)