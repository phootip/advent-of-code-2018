import datetime
import pprint
pp = pprint.PrettyPrinter()

logs = {}
guards = {}

f = open("4.txt","r")
for line in f:
  log = line.split()
  time = datetime.datetime.strptime(log[0]+' '+log[1],'[%Y-%m-%d %H:%M]')
  logs[time] = log[2:]

logs = sorted(logs.items())

cGuard = 0
for log in logs:
  act = log[1]
  if act[0] == "Guard":
    cGuard = int(act[1][1:])
    if(not cGuard in guards): guards[cGuard] = {}
  elif act[0] == "falls":
    falls = log[0]
  elif act[0] == "wakes":
    wakes = log[0]
    while wakes != falls:
      key = str(falls.hour) + ':' + str(falls.minute)
      if key in guards[cGuard]:
        guards[cGuard][key] += 1
      else:
        guards[cGuard][key] = 1
      falls += datetime.timedelta(minutes=1)

mguard = 0
cmax = 0
for guard in guards:
  cguard = guard
  guard = guards[guard]
  if not guard:
    continue
  pp.pprint(guard)
  gmax = guard[max(guard, key=guard.get)]
  if gmax > cmax:
    cmax = gmax
    mguard = cguard

print(mguard)
print(cmax)
print(guards[mguard])
print(30*mguard)