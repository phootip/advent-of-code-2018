class Node:
  def __init__(self, id, parent, n_child, n_metadata):
    self.id = id
    self.parent = parent
    self.n_child = n_child
    self.n_metadata = n_metadata
    self.metadata = []
    self.childs = []
    self.value = None
  
  def addChild(self,node):
    self.childs.append(node)
  
  def __str__(self):
    if (self.parent): parent = self.parent.id
    else: parent = None
    return '(id={}, parent={}, n_child={}, n_metadata={}, metadata={})'.format(self.id, parent,
    self.n_child,self.n_metadata,self.metadata)
  
  def getValue(self):
    if(self.value):
      return self.value
    if(self.n_child == 0):
      self.value = sum(self.metadata)
    else:
      result = 0
      for i in self.metadata:
        if(0<i<=len(self.childs)):
          result += self.childs[i-1].getValue()
      self.value = result
    return self.value