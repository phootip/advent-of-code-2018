from settings import maps,units,adjacent
import pprint
pp = pprint.PrettyPrinter().pprint

class Unit:
  def __init__(self,kind,x,y):
    self.kind = kind
    self.x = x
    self.y = y
    self.hp = 200
    self.atk = 3
    self.dead = False

  def __lt__(self,other):
    return self.y < other.y or (self.y == other.y and self.x < other.x)
  
  def __str__(self):
    return f'{self.kind} ({self.x},{self.y}) hp:{self.hp}'

  def move(self):
    if(self.getOpponent()):
      return
    dest = set()
    for unit in units:
      if(self.kind != unit.kind and not unit.dead):
        dest = dest.union(set(unit.atkRange()))
    next_pos = self.shortestPath(dest)
    maps[self.y][self.x] = '.'
    maps[next_pos[1]][next_pos[0]] = self.kind
    self.x,self.y = next_pos
    return
  
  def shortestPath(self,dest):
    que = [[(self.x,self.y)]]
    visited = [(self.x,self.y)]
    while que:
      que = sorted(que, key= lambda i: (len(i),i[0][1],i[0][0]))
      path = que.pop(0)
      node = path[-1]
      adj = adjacent(node)
      for i in adj:
        if(not i in visited):
          visited.append(i)
          new_path = path[:]
          new_path.append(i)
          que.append(new_path)
          if(i in dest):
            return new_path[1]
    return (self.x,self.y)
  
  def attack(self):
    opponent = self.getOpponent()
    if(opponent):
      opponent.hp -= self.atk
      if(opponent.hp <= 0):
        opponent.dead = True
        x,y = opponent.x, opponent.y
        maps[y][x] = '.'
    return
  
  def getOpponent(self):
    x,y = self.x,self.y
    if(self.kind == 'E'): other = 'G'
    else: other = 'E'
    temp = []
    if(maps[y-1][x] == other):
      temp += [i for i in units if i.x == x and i.y == y-1 and i.hp > 0]
    if(maps[y][x-1] == other):
      temp += [i for i in units if i.x == x-1 and i.y == y and i.hp > 0]
    if(maps[y][x+1] == other):
      temp += [i for i in units if i.x == x+1 and i.y == y and i.hp > 0]
    if(maps[y+1][x] == other):
      temp += [i for i in units if i.x == x and i.y == y+1 and i.hp > 0]
    if(temp):
      # return min(temp,key= lambda i: i.hp)
      min_hp = 300
      node = None
      for i in temp:
        if(i.hp < min_hp):
          min_hp = i.hp
          node = i
      return node
    else:
      return None

  def atkRange(self):
    return adjacent((self.x,self.y))
  
  def removeDead(self):
    global units
    units = list(filter(lambda unit : not unit.dead, units))
    units = sorted(units,key= lambda i : (i.y,i.x))