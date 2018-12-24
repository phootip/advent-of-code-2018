from opController import opTester

f = open('16-1.txt')
# f = open('16-test.txt')
ans = 0

def before(line):
  global ans
  reg = [line[1][1], line[2][0], line[3][0], line[4][0]]
  reg = list(map(int,reg))
  inst = f.readline().strip().split()
  inst = list(map(int,inst))
  line = f.readline().strip().split()
  reg2 = [line[1][1], line[2][0], line[3][0], line[4][0]]
  reg2 = list(map(int,reg2))
  ans += opTester(inst,reg,reg2)

switch =  {
  'Before:': before
}

while True:
  line = f.readline().strip().split()
  if line:
    switch.get(line[0])(line)
  else:
    print(ans)
    break
