import string

f = open('./5-2.txt')
data = f.read()

def reaction(data):
  for i in range(len(data)-1):
    if((data[i].isupper() and data[i].lower() == data[i+1]) or 
    (data[i].islower() and data[i].upper() == data[i+1])):
      return data[:i] + data[i+2:]
  return data

current_min = 999999
for char in string.ascii_lowercase:
  print(char)
  data2 = data.replace(char,'').replace(char.upper(),'')
  cdata = ''
  while cdata != data2:
    # print(len(data2))
    cdata = data2
    data2 = reaction(data2)
  current_min = min(current_min,len(data2))

print(current_min)