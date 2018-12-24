import opController
opcode = [{'gtrr', 'gtri', 'addi', 'bori', 'addr', 'borr', 'setr', 'seti', 'gtir'}, {'eqir', 'addi', 'bori', 'eqrr'}, {'gtrr', 'seti', 'gtri'}, {'muli'}, {'seti', 'borr', 'eqri', 'addr', 'eqir'}, {'borr', 'bori'}, {'addi', 'bori'}, {'mulr'}, {'gtrr', 'seti', 'eqri'}, {'seti', 'borr', 'addi', 'bori'}, {'gtrr', 'bani', 'muli', 'gtri', 'addi', 'addr', 'mulr', 'bori', 'borr', 'banr', 'setr', 'seti', 'gtir'}, {'seti', 'eqri'}, {'mulr', 'addi', 'addr', 'muli'}, {'gtrr', 'eqri', 'gtri', 'eqir', 'seti', 'gtir', 'eqrr'}, {'addi', 'mulr'}, {'bani', 'gtrr', 'eqri', 'muli', 'bori', 'addr', 'borr', 'setr'}]
visited = set()

for i in range(16):
  for j in range(16):
    if(len(opcode[j]) == 1 and not opcode[j].intersection(visited)):
      # print('op:',j)
      # print(opcode[j])
      for k in range(16):
        if j == k: continue
        opcode[k].difference_update(opcode[j])

opcode = list(map(lambda x: x.pop(),opcode))
print(opcode)
reg = [0,0,0,0]
f = open('16-2.txt')

for line in f:
  op, *arg = list(map(int,line.split()))
  inst = opcode[op]
  # print(inst)
  getattr(opController,inst)(*arg,reg,reg,set())

print(reg)