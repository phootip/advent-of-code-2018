# import requests
# r = requests.get("https://adventofcode.com/2018/day/5/input")

# never mind, puzzle input differ by user.

f = open('./5-1.txt')
data = f.read()

def reaction(data):
  for i in range(len(data)-1):
    if((data[i].isupper() and data[i].lower() == data[i+1]) or 
    (data[i].islower() and data[i].upper() == data[i+1])):
      return data[:i] + data[i+2:]
  return data

cdata = ''
while cdata != data:
  print(len(data))
  cdata = data
  data = reaction(data)

print(len(cdata))
print(data)