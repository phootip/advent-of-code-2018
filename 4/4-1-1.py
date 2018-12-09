from datetime import datetime
import pprint
pp = pprint.PrettyPrinter()

logs = {}
guards = {}

f = open("4.txt","r")
for line in f:
  log = line.split()
  time = datetime.strptime(log[0]+' '+log[1],'[%Y-%m-%d %H:%M]')
  logs[time] = log[2:]

logs = sorted(logs.items())

cGuard = 0
falls = 0
wakes = 0
for log in logs:
  act = log[1]
  if act[0] == "Guard":
    cGuard = int(act[1][1:])
    if(not cGuard in guards): guards[cGuard] = 0
  elif act[0] == "falls":
    falls = log[0]
  elif act[0] == "wakes":
    wakes = log[0]
    guards[cGuard] += (wakes - falls).total_seconds()
  
#3167 is super lazy



pp.pprint(max(guards,key = guards.get))

