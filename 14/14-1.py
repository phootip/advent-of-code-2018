s = 190221
# s = 9
# s = 18

data = [3,7]
elf1 = 0
elf2 = 1
while len(data) < s + 10:
  recipe = data[elf1] + data[elf2]
  for ch in str(recipe):
    data.append(int(ch))
  elf1 += data[elf1] + 1
  elf1 %= len(data)
  elf2 += data[elf2] + 1
  elf2 %= len(data)

print(''.join([str(i) for i in data[-10:]]))