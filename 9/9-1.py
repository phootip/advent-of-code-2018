# n_players = 411
# last_marble = 69
# 1 -> 10112
# 10 -> 425688
# 100 -> 36226337
# 1000 -> 

# high score = 32
# n_players = 9
# last_marble = 25
n_players = 9
last_marble = 46
# high score = 8317
# n_players = 10
# last_marble = 1618

players = [0 for i in range(n_players)]
marbles = [0]
position = 0
c_marble = 1
player = 0

while c_marble < last_marble+1:
  if(c_marble % 23 == 0):
    players[player] += c_marble
    position -= 7
    if(position < 0): 
      position += len(marbles)
    players[player] += marbles.pop(position)
    print('c_marble:',c_marble)
    print('players[player]:',players[player])
  else:  
    position += 2
    position %= len(marbles)
    marbles.insert(position, c_marble)
  player += 1
  player %= len(players)
  c_marble += 1

print(max(players))
print(players)