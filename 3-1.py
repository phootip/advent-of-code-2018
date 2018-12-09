farbic = [[0]*1000 for i in range(1000)]
loop = 0
data = {}
while True:
  a = input()
  if(a == ''):
    break
  token = a.split()
  id = int(token[0][1:])
  position = token[2][:-1]
  position = list(map(int,position.split(',')))
  size = list(map(int,token[-1].split('x')))
  data[id] = {'position':position,'size':size}

  overlap = False
  for height in range(size[1]):
    for width in range(size[0]):
      farbic[position[1]+height][position[0]+width] += 1

for i in range(1,len(data)+1):
  ans = True
  position = data[i]['position']
  size = data[i]['size']
  # print('position:',position)
  # print('size:',size)
  for height in range(size[1]):
    for width in range(size[0]):
      if(farbic[position[1]+height][position[0]+width] != 1):
        ans = False
  if(ans):
    print(i)
