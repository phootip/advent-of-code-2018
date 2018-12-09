twice = 0
trice = 0
while True:
  char = {}
  a = input()
  if( a == '' ): break
  for i in a:
    if(not i in char):
      char[i] = 1
    else:
      char[i] += 1
  print(char)

  ctwice = False
  ctrice = False
  for i in char.values():
    if(i == 2): ctwice = True
    elif(i == 3): ctrice = True
  if(ctwice): twice += 1
  if(ctrice): trice += 1

print('twice:', twice)
print('trice:', trice)
print(twice * trice)
  