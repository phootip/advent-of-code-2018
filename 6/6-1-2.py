import pprint
import math
import numpy
pp = pprint.PrettyPrinter(depth=3)

f = open('6-1.txt')
# 4284
# f = open('6-1-2.txt')
# f = open('6-test.txt')
data = []

for line in f:
  data.append(list(map(int,line.replace(' ','').strip().split(','))))

maxX = minX = data[0][0]
maxY = minY = data[0][1]

for cor in data:
  maxX = max(maxX,cor[0])
  minX = min(minX,cor[0])
  
  maxY = max(maxY,cor[1])
  minY = min(minY,cor[1])
  
print(minX,minY)
# 40 50
for i in range(len(data)):
  data[i] = [data[i][0] - minX,data[i][1] - minY]

maxX = minX = data[0][0]
maxY = minY = data[0][1]

for cor in data:
  maxX = max(maxX,cor[0])
  minX = min(minX,cor[0])
  
  maxY = max(maxY,cor[1])
  minY = min(minY,cor[1])
  
print(maxX,maxY)
plane = [[[0] for j in range(maxX+1)] for i in range(maxY+1)]
# plane = numpy.zeros((maxY+1,maxX+1,1))

def distant(cor,x,y):
  # return math.hypot(cor[0]-x,cor[1]-y)
  return abs(cor[0]-x) + abs(cor[1]-y)
  
for point in range(len(data)):
  print('point',point)
  cor = data[point]
  plane[cor[1]][cor[0]] = [point]
  for i in range(len(plane)):
    for j in range(len(plane[i])):
      if(point in plane[i][j]):
        continue
      current_point = int(plane[i][j][0])
      cor2 = data[current_point]
      if distant(cor,j,i) < distant(cor2,j,i):
        plane[i][j] = [point]
      elif distant(cor,j,i) == distant(cor2,j,i):
        plane[i][j].append(point)
      

# pp.pprint(plane)
# plane[0][0].append(1)
# pp.pprint(plane)

edge = set()
for i in plane[0]:
  if len(i) == 1:
    edge.add(i[0])
for i in plane[-1]:
  if len(i) == 1:
    edge.add(i[0])
for i in range(1,len(plane)-1):
  if len(plane[i][0]) == 1:
    edge.add(plane[i][0][0])
  if len(plane[i][-1]) == 1:
    edge.add(plane[i][-1][0])
print(list(edge))

ans = 0
for point in range(len(data)):
  cmax = 0
  if point in edge:
    continue
  for i in plane:
    for j in i:
      if([point] == j):
        cmax += 1
  print(point,cmax)
  ans = max(ans,cmax)

print(ans)