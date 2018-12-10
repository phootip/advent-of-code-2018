class Node:
  def __init__(self,data,next=None,prev=None):
    self.data = data
    self.next = next
    self.prev = prev
  def __str__(self):
    return 'data: {}, next: {}, prev: {}'.format(self.data, self.next.data, self.prev.data)

class LinkList:
  def __init__(self):
    self.head = None
  
  def append(self,data):
    return
  
  def insert(self,index,data):
    if(self.head is None):
      self.head = Node(data)
      self.head.next = self.head.prev = self.head
    else:
      node = self.head
      for i in range(index):
        return
    return

  def pop(self,index):
    return