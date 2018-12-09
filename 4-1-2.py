import datetime
import pprint
pp = pprint.PrettyPrinter()

logs = {}
times = {}

f = open("4.txt","r")
for line in f:
  log = line.split()
  time = datetime.datetime.strptime(log[0]+' '+log[1],'[%Y-%m-%d %H:%M]')
  logs[time] = log[2:]

logs = sorted(logs.items())

for log in logs:
  act = log[1]
  if act[0] == "Guard":
    cGuard = int(act[1][1:])
  if cGuard != 3167:
    continue
  
  if act[0] == "falls":
    falls = log[0]
  elif act[0] == "wakes":
    wakes = log[0]
    while wakes != falls:
      key = str(falls.hour) + ':' + str(falls.minute)
      if key in times:
        times[key] += 1
      else:
        times[key] = 1
      falls += datetime.timedelta(minutes=1)

print(max(times,key=times.get))
print(times['0:45'])

print(45*3167)