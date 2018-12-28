from tkinter import *
import copy
import time

# f = open('./17/17.txt')
f = open('./17.txt')
# f = open('17-test.txt')

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
      maps[i][p1] = '@'
  else:
    for i in range(p21,p22+1):
      maps[p1][i] = '@'

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

root = Tk()
canvas = Canvas(root, width=750, height=750, background='black')
ref = set()
canvas.pack()

def draw():
  for y in range(minY,maxY+1):
    for x in range(minX,maxX+1):
      # print(maps[y][x],end='')
      if(maps[y][x] == '+' or maps[y][x] == '@'):
        if(maps[y][x] == '+'):
          maps[y][x] = '|'
        if(maps[y][x] == '@'):
          maps[y][x] = '#'
        cx,cy = x,y
        cx -= 425
        cx *= 5
        cy *= 5
        if(maps[y][x] != '#'):
          point = canvas.create_oval(cx,cy,cx+5,cy+5, fill = 'blue',outline='white')
        else:
          point = canvas.create_oval(cx,cy,cx+5,cy+5, fill = 'brown',outline='white')
        ref.add(point)

def cycle():
  global maps
  for y in range(minY,maxY+1):
    for x in range(minX,maxX+1):
      if maps[y][x] == '|':
        if(maps[y+1][x] == '.'):
          maps[y+1][x] = '+'
        
draw()
canvas.update()
loop = 0
while True:
  start = time.clock()
  
  loop += 1
  cycle()

  mid = time.clock()
  
  draw()
  canvas.update()
  # canvas.after(100)
  
  end = time.clock()
  print('cycle:',loop)
  print('cal:',mid - start)
  print('time:',end - start)

root.mainloop()


print(minX,minY)
print(maxX,maxY)