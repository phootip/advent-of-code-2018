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
plane = [[0 for j in range(maxX+1)] for i in range(maxY+1)]
# plane = numpy.zeros((maxY+1,maxX+1,1))

def distant(cor,x,y):
  # return math.hypot(cor[0]-x,cor[1]-y)
  return abs(cor[0]-x) + abs(cor[1]-y)

ans = 0
for y in range(len(plane)):
  for x in range(len(plane[0])):
    print('x,y:',x,y)
    for point in range(len(data)):
      cor = data[point]
      plane[y][x] += distant(cor,x,y)
    if(plane[y][x] < 10000):
      ans += 1
print(ans)