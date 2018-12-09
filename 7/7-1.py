data = {}

# f = open('./7/7.txt')
f = open('./7/7-test.txt')
for line in f:
  token = line.split()
  first = token[1]
  second = token[7]
  if(not first in data):
    data[first] = [second]
  else:
    data[first].append(second)
  if(not second in data):
    data[second] = []

done = []
doing = []
for first in data:
  starter = True
  for value in data.values():
    if(first in value):
      starter = False
      break
  if(starter):
    print('starter', first)
    doing.append(first)


while doing:
  print(doing)
  current = ''
  for i in range(len(doing)):
    node = doing[i]
    do = True
    for value in data.values():
      if(node in value):
        do = False
        break
    if(do):
      current = doing.pop(i)
      print(current)
      break
  doing += data.pop(current)
  doing = list(set(doing))
  doing.sort()
  done.append(current)
  # print(data)
  # print('doing:',doing)
  # print('done:',done)

# print(data)
# print(doing)
print(''.join(done))
  
