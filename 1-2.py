arr = []
while True:
  a = input()
  if(a == ''): break
  arr.append(int(a))

print('calculating')

def cal():
  freq = 0
  past = []
  while True:
    for i in arr:
      freq += i
      if(not freq in past): 
        past.append(freq)
        print(freq)
        # print(past)
      else: 
        return freq

print(cal())
