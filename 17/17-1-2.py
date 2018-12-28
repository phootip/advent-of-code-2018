from tkinter import *
import copy
import time
from PIL import Image, ImageDraw
import imageio
import os
import pyglet

# f = open('./17/17.txt')
# f = open('./17.txt')
f = open('17-test.txt')

maps = [['.' for i in range(2000)] for j in range(2000)]
for line in f:
  line = line.strip().split(',')
  line = list(map(lambda x: x.strip().split('='),line))
  line[1][1] = list(map(int,line[1][1].split('..')))
  line[0][1] = int(line[0][1])
  # print(line)
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

def draw(loop):
  ans = 0
  im = Image.new('RGB', (2000, 2000), color = 'white')
  draw = ImageDraw.Draw(im)
  for y in range(minY,maxY+1):
    for x in range(minX-1,maxX+2):
      # print(maps[y][x],end='')
      if(maps[y][x] == '|'):
        draw.rectangle([(x,y),(x,y)],fill='red')
        ans += 1
      elif(maps[y][x] == '#'):
        draw.rectangle([(x,y),(x,y)],fill='brown')
        ans += 0
      elif(maps[y][x] == '~'):
        draw.rectangle([(x,y),(x,y)],fill='blue')
        ans += 1
    # print()
  im = im.crop((450,0,550,100))
  im = im.resize((500,500))
  im.save(f"./visual/visual-{'0'*(5-len(str(loop)))}{loop}.png")
  return ans

def cycle():
  global maps,ans
  temp = []
  for y in range(minY,maxY+1):
    for x in range(minX,maxX+1):
      if maps[y][x] == '|':
        if(maps[y+1][x] == '.'):
          temp.append((x,y+1,'|'))
          maps[y+1][x] = '|'
        elif maps[y+1][x] == '#' or maps[y+1][x] == '~':
          if(maps[y][x-1] == '.'):
            temp.append((x-1,y,'|'))
            maps[y][x-1] = '|'
          elif(maps[y][x-1] == '#'):
            x2 = x
            while maps[y][x2] == '|':
              x2 += 1
            if(maps[y][x2]) == '#':
              for i in range(x,x2):
                maps[y][i] = '~'
                temp.append((i,y,'~'))
          if(maps[y][x+1] == '.'):
            maps[y][x+1] = '|'
            temp.append((x+1,y,'|'))
  for x,y,i in temp:
    maps[y][x] = i
  if temp: return False
  else: return True
        

files = os.listdir('./visual')
for f in files:
  os.remove(f'./visual/{f}')
loop = 0
draw(loop)
while True:
  # start = time.perf_counter()
  loop += 1
  e = cycle()
  # mid = time.perf_counter()
  # # ans = draw(loop)
  # end = time.perf_counter()
  print('cycle:',loop)
  if(e):
    break
  # print('cal:',mid - start)
  # print('draw:',end - mid)

def gif():
  files = os.listdir('./visual')
  with imageio.get_writer('./movie.gif', mode='I') as writer:
    for filename in files:
      print(filename)
      image = imageio.imread(f'./visual/{filename}')
      writer.append_data(image)

# gif()
animation = pyglet.image.load_animation('movie.gif')
animSprite = pyglet.sprite.Sprite(animation)
w = animSprite.width
h = animSprite.height
window = pyglet.window.Window(w,h)


@window.event
def on_draw():
  window.clear()
  animSprite.draw()

pyglet.app.run()
print(minX,minY)
print(maxX,maxY)
ans = draw(loop)
print(ans - 1)