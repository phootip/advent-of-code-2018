from cart import Cart, Track
f = open('13.txt')
# f = open('13-test.txt')

maps = [['' for i in range(160)] for j in range(160)]
carts = []
j = 0

for line in f:
  for i in range(len(line)):
    if(line[i] in ['>','<','v','^']):
      if(line[i] == '>'):
        cart = Cart(i,j,'x',1)
        maps[j][i] = '-'
      elif(line[i] == '<'):
        cart = Cart(i,j,'x',-1)
        maps[j][i] = '-'
      elif(line[i] == 'v'):
        cart = Cart(i,j,'y',1)
        maps[j][i] = '|'
      else:
        cart = Cart(i,j,'y',-1)
        maps[j][i] = '|'
      carts.append(cart)
    else:
      maps[j][i] = line[i].strip()
  j += 1

# game start
def start():
  tick = 0
  while True:
    carts.sort()
    for cart in carts:
      cart.move()
      x,y = cart.x, cart.y
      for cart2 in carts:
        if(cart != cart2 and x == cart2.x and  y == cart2.y):
          return (x,y)
      if maps[y][x] == '/':
        cart.direc = -cart.direc
        cart.turn()
      elif maps[y][x] == '\\':
        cart.turn()
      elif maps[y][x] == '+':
        cart.intersec()
    tick += 1
    print(tick)
    # print(carts[0])
      

print(start())
# print(carts[0])
# print(carts[1])