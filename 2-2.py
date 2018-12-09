arr = []
while True:
  a = input()
  if a == '':
    break
  for string in arr:
    diff = 0
    for i in range(len(string)):
      if( string[i] != a[i]):
        diff += 1
    if diff == 1:
      print('string: ', string)
      print('current: ', a)
      exit()
  arr.append(a)