import pprint
from node import Node
pp = pprint.PrettyPrinter().pprint

nodes = []
stack = []
stack2 = []
f = open('8.txt')
# f = open('8-test.txt')
data = list(map(int,f.read().split()))

root = Node(0,None,data.pop(0),data.pop(0))
stack.append(root)
while stack:
  # print(data)
  # print(stack)
  
  node = stack[-1]
  print(len(stack2))
  if(node.n_child == 0):
    stack2.append(stack.pop())
    for i in range(node.n_metadata):
      node.metadata.append(data.pop(0))
  else:
    next_node = Node(node.id + node.n_child, node, data.pop(0), data.pop(0))
    node.n_child -= 1
    stack.append(next_node)

ans = 0
for node in stack2:
  for k in node.metadata:
    ans += k

print(ans)