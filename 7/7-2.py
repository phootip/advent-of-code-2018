data = {}

# f = open('./7/7.txt')
f = open('7.txt')
# f = open('7-test.txt')
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
workers = [['',0] for i in range(5)]
time = 0
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
  for i in range(len(doing)):
    node = doing[i]
    do = True
    for worker in workers:
      if(worker[0] == node):
        do = False
        break
    for value in data.values():
      if(node in value):
        do = False
        break
    if(do):
      for j in range(len(workers)):
        if(workers[j][0] == ''):
          workers[j] = [node, ord(node)-4]
          break
  min_time = 99
  for worker in workers:
    if(worker[0] != ''):
      min_time = min(min_time,worker[1])
  time += min_time
  for i in range(len(workers)):
    if(workers[i][0] != ''):
      workers[i][1] -= min_time
      if(workers[i][1] == 0):
        node = workers[i][0]
        workers[i][0] = ''
        print('node:',node)
        doing.remove(node)
        doing += data.pop(node)
        done.append(node)
  # print(workers)
  print(time)
  doing = list(set(doing))
  doing.sort()
  # doing += data.pop(node)
  # doing = list(set(doing))
  # doing.sort()
  # done.append(node)
  # print(data)
  # print('doing:',doing)
  # print('done:',done)

# print(data)
# print(doing)
print(''.join(done))
print(time)
  
