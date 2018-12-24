opcode = [{
  'addr',
  'addi',
  'mulr',
  'muli',
  'banr',
  'bani',
  'borr',
  'bori',
  'setr',
  'seti',
  'gtir',
  'gtri',
  'gtrr',
  'eqir',
  'eqri',
  'eqrr',
  } for i in range(16)]
# print(opcode)

def opTester(inst,reg,reg2):
  ans = 0
  buffer = set()
  ans += addr(*inst[1:],reg[:],reg2,buffer)
  ans += addi(*inst[1:],reg[:],reg2,buffer)
  ans += mulr(*inst[1:],reg[:],reg2,buffer)
  ans += muli(*inst[1:],reg[:],reg2,buffer)
  ans += banr(*inst[1:],reg[:],reg2,buffer)
  ans += bani(*inst[1:],reg[:],reg2,buffer)
  ans += borr(*inst[1:],reg[:],reg2,buffer)
  ans += bori(*inst[1:],reg[:],reg2,buffer)
  ans += setr(*inst[1:],reg[:],reg2,buffer)
  ans += seti(*inst[1:],reg[:],reg2,buffer)
  ans += gtir(*inst[1:],reg[:],reg2,buffer)
  ans += gtri(*inst[1:],reg[:],reg2,buffer)
  ans += gtrr(*inst[1:],reg[:],reg2,buffer)
  ans += eqir(*inst[1:],reg[:],reg2,buffer)
  ans += eqri(*inst[1:],reg[:],reg2,buffer)
  ans += eqrr(*inst[1:],reg[:],reg2,buffer)
  op = inst[0]
  print(buffer)
  opcode[op].intersection_update(buffer)
  print(opcode)
  return 1 if ans >= 3 else 0

def addr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = x + y
  if(reg == reg2): 
    buffer.add('addr')
    return 1
  return 0

def addi(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = x + y
  if(reg == reg2): 
    buffer.add('addi')
    return 1
  return 0

def mulr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = x * y
  if(reg == reg2): 
    buffer.add('mulr')
    return 1
  return 0

def muli(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = x * y
  if(reg == reg2): 
    buffer.add('muli')
    return 1
  return 0

def banr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = x & y
  if(reg == reg2): 
    buffer.add('banr')
    return 1
  return 0

def bani(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = x & y
  if(reg == reg2): 
    buffer.add('bani')
    return 1
  return 0

def borr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = x | y
  if(reg == reg2): 
    buffer.add('borr')
    return 1
  return 0

def bori(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = x | y
  if(reg == reg2): 
    buffer.add('bori')
    return 1
  return 0

def setr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  # y = reg[b]
  reg[c] = x
  if(reg == reg2): 
    buffer.add('setr')
    return 1
  return 0

def seti(a,b,c,reg,reg2,buffer):
  x = a
  # y = b
  reg[c] = x
  if(reg == reg2): 
    buffer.add('seti')
    return 1
  return 0

def gtir(a,b,c,reg,reg2,buffer):
  x = a
  y = reg[b]
  reg[c] = 1 if x > y else 0
  if(reg == reg2): 
    buffer.add('gtir')
    return 1
  return 0

def gtri(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = 1 if x > y else 0
  if(reg == reg2): 
    buffer.add('gtri')
    return 1
  return 0

def gtrr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = 1 if x > y else 0
  if(reg == reg2): 
    buffer.add('gtrr')
    return 1
  return 0

def eqir(a,b,c,reg,reg2,buffer):
  x = a
  y = reg[b]
  reg[c] = 1 if x == y else 0
  if(reg == reg2): 
    buffer.add('eqir')
    return 1
  return 0

def eqri(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = b
  reg[c] = 1 if x == y else 0
  if(reg == reg2): 
    buffer.add('eqri')
    return 1
  return 0

def eqrr(a,b,c,reg,reg2,buffer):
  x = reg[a]
  y = reg[b]
  reg[c] = 1 if x == y else 0
  if(reg == reg2): 
    buffer.add('eqrr')
    return 1
  return 0
