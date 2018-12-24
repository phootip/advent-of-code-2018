# s = 190221
# s = 51589
s = 515891
# s = 59414

data = [3,7]
l = len(str(s))
elf1 = 0
elf2 = 1
while True:
  recipe = data[elf1] + data[elf2]
  for ch in str(recipe):
    data.append(int(ch))
  elf1 += data[elf1] + 1
  elf1 %= len(data)
  elf2 += data[elf2] + 1
  elf2 %= len(data)
  print(elf1)
  if(len(data) >= l):
    last = int(''.join([str(i) for i in data[-l:]]))
    last2 = int(''.join([str(i) for i in data[-l-1:-1]]))
    if(last == s):
      print(len(data) - l)
      exit()
    elif(last2 == s):
      print('last2')
      print(len(data) - l - 1)
      exit()