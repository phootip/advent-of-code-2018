
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
  pots = next_pots

for i in range(20):
  addLeft()
  addRight()
  nextGen()
print('left:',left_most)
print(pots)

ans = 0
for i in range(len(pots)):
  if(pots[i] == '#'):
    ans += left_most + i
print(ans)