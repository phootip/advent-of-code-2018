import re
from star import Star

f = open('10.txt')
# f = open('10-test.txt')

stars = []
for line in f:
  x,y,vX,vY = [int(i) for i in re.findall(r'[-+]?[0-9]+',line)]
  stars.append(Star(x,y,vX,vY))

def update(n = 1):
  for star in stars:
    star.x += star.vX*n
    star.y += star.vY*n

def checkAlign():
  for star in stars:
    align = True
    align = checkPosition(star.x,star.y+1) and align
    align = checkPosition(star.x,star.y+2) and align
    align = checkPosition(star.x,star.y+3) and align
    align = checkPosition(star.x,star.y+4) and align
    align = checkPosition(star.x,star.y+5) and align
    align = checkPosition(star.x,star.y+6) and align
    if(align): return True
  return False

def checkPosition(x,y):
  for star in stars:
    if(star.x == x and star.y == y):
      return True
  return False

def visualize():
  left = min([star.x for star in stars])
  right = max([star.x for star in stars])
  top = min([star.y for star in stars])
  down = max([star.y for star in stars])
  print(left,right)
  for y in range(top,down+1):
    line = ''
    for x in range(left,right+1):
      if(checkPosition(x,y)):
        line += '#'
      else:
        line += '.'
    print(line)

update(10330)
sec = 0
while True:
  update()
  sec += 1
  print(sec)
  if(checkAlign()):
    break

visualize()