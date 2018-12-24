class Node:
  def __init__(self,data,next=None,prev=None):
    self.data = data
    self.next = next
    self.prev = prev
  
  def __str__(self):
    return f'data:{self.data}, prev,next: ({self.prev},{self.next})'
