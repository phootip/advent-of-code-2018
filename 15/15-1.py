from unit import Unit
import pprint
from settings import maps,units

pp = pprint.PrettyPrinter().pprint

# f = open('15.txt')
# f = open('15-test-1.txt')
f = open('15-test-2.txt')
# f = open('15-test-3.txt')
# f = open('15-test-4.txt')
# f = open('15-test-5.txt')
# f = open('15-test-6.txt')
y = 0
for line in f:
  temp = []
  x = 0
  for ch in line.strip():
    if(ch != 'E' and ch != 'G'):
      temp.append(ch)
    else:
      unit = Unit(ch,x,y)
      units.append(unit)
      temp.append(ch)
    x += 1
  maps.append(temp)
  y += 1

n_round = 0
while True:
  n_round += 1
  print('round:',n_round)
  for unit in units:
    if(unit.dead):
      print('unit is dead:',unit)
      continue
    else:
      unit.move()
      unit.attack()
  
  units = list(filter(lambda unit : not unit.dead, units))
  units = sorted(units,key= lambda i : (i.y,i.x))
  units[0].removeDead()

  # for debug
  pp(maps)
  for unit in units:
    print(unit)
  # Check end game
  kind = units[0].kind
  end = True
  for unit in units[1:]:
    if(unit.kind != kind):
      end = False
  if(end):
    total_hp = 0
    for unit in units:
      total_hp += unit.hp
    print(total_hp)
    print(n_round)
    print(total_hp*n_round)
    exit()
