
global maps,units,adjacent
maps,units = [],[]

def adjacent(point):
  x,y = point
  temp = []
  if(maps[y-1][x] == '.'):
    temp.append((x,y-1))
  if(maps[y][x-1] == '.'):
    temp.append((x-1,y))
  if(maps[y][x+1] == '.'):
    temp.append((x+1,y))
  if(maps[y+1][x] == '.'):
    temp.append((x,y+1))
  return temp
