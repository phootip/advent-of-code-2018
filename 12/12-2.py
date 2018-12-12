
f = open('12.txt')
# f = open('12-test.txt')

pots = f.readline().split()[2].strip()
f.readline()

rules = {}
left_most = 0
for line in f:
  rule, next_gen = line.strip().split(' => ')
  rules[rule] = next_gen

def addLeft():
  global pots, left_most
  first = 0
  for i in range(len(pots)):
    if(pots[i] == '#'):
      first = i
      break
  first = first - 4
  left_most += first
  if(first < 0):
    first = abs(first)
    pots = '.' * first + pots
  else:
    pots = pots[first:]

def addRight():
  global pots, left_most
  last = 0
  for i in range(len(pots)-1, -1, -1):
    if(pots[i] == '#'):
      last = i
      break
  last = last + 4
  if(last > len(pots)-1):
    last -= len(pots)-1
    last = abs(last)
    pots += '.' * last
  else:
    pots = pots[:last + 1]

def nextGen():
  global pots
  next_pots = '..'
  for i in range(len(pots) - 4):
    match = False
    for j in rules:
      if(j == pots[i:i+5]):
        next_pots += rules[j]
        match = True
        break
    if(not match):
      # next_pots += pots[i+2]
      next_pots += '.'
  # if(pots == next_pots[1:]+'...'):
    # print('same state:',left_most)
    # exit()
    # print(pots)
  pots = next_pots

def cal():
  ans = 0
  for i in range(len(pots)):
    if(pots[i] == '#'):
      ans += left_most + i
  return ans

x,y = 0,0
for i in range(50000000000):
  addLeft()
  addRight()
  nextGen()
  # print(i)
  if(i == 120 or i == 121 or i == 122 or i == 123):
    print('i',i)
    print('left:',left_most)
    print(pots)
  x = cal()
  if(x-y == 58):
    print(i)
    break
  y = x

print(cal())
print('left:',left_most)
print(pots)
print(8932 + 58 * (50000000000 - 122))