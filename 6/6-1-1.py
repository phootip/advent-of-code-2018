import pprint
import math
import sys
# hahahaha stack overflow
sys.setrecursionlimit(9000)
pp = pprint.PrettyPrinter(depth=3)

# f = open('6-1.txt')
f = open('./6/6-test.txt')
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
  
# print(minX,minY)
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
plane = [[[0]]*(maxX+1) for i in range(maxY+1)]

def distant(cor,x,y):
  # return math.hypot(cor[0]-x,cor[1]-y)
  return abs(cor[0]-x) + abs(cor[1]-y)

def calClosest(point,x,y):
  # print('x,y:',x,y)
  if(x < 0 or y < 0 or x > maxX or y > maxY):
    return
  if(point in plane[y][x]):
    return
  cor = data[point]
  current_point = plane[y][x][0]
  cor2 = data[current_point]
  if distant(cor,x,y) < distant(cor2,x,y):
    plane[y][x] = [point]
    calClosest(point,x+1,y)
    calClosest(point,x-1,y)
    calClosest(point,x,y+1)
    calClosest(point,x,y-1)
    return
  elif distant(cor,x,y) == distant(cor2,x,y):
    plane[y][x].append(point)
    return
  else:
    return

for point in range(1,len(data)):
  [x,y] = data[point]
  plane[y][x] = [point]
  calClosest(point,x+1,y)
  calClosest(point,x-1,y)
  calClosest(point,x,y+1)
  calClosest(point,x,y-1)
# pp.pprint(plane)

edge = set()
for i in plane[0]:
  if len(i) == 1:
    edge.add(i[0])
for i in plane[-1]:
  if len(i) == 1:
    edge.add(1)
for i in range(1,len(plane)-1):
  if len(plane[i][0]) == 1:
    edge.add(plane[i][0][0])
  if len(plane[i][-1]) == 1:
    edge.add(plane[i][-1][0])
# print(list(edge))

ans = 0
for point in range(len(data)):
  cmax = 0
  if point in edge:
    continue
  for i in plane:
    for j in i:
      if([point] == j):
        cmax += 1
  ans = max(ans,cmax)

print(ans)