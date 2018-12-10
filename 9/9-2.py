from linkedList import Node

# high score = 32
# n_players = 9
# last_marble = 25
# n_players = 9
# last_marble = 46
# high score = 8317
# n_players = 10
# last_marble = 1618
# high score = 425688
n_players = 411
last_marble = 71170*100

players = [0 for i in range(n_players)]
player = 0
node = Node(0)
node.next = node
node.prev = node

c_marble = 1
while c_marble <= last_marble:
  if(not c_marble % 23):
    players[player] += c_marble
    for i in range(7):
      node = node.prev
    players[player] += node.data
    node.prev.next = node.next
    node.next.prev = node.prev
    node = node.next
    a = node.data
  else:
    new_node = Node(c_marble, node.next.next, node.next)
    node.next.next.prev = new_node
    node.next.next = new_node
    node = new_node
  player += 1
  player %= len(players)
  c_marble += 1

print(max(players))