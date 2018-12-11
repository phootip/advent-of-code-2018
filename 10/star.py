class Star:
  def __init__(self,x,y,vX,vY):
    self.x = x
    self.y = y
    self.vX = vX
    self.vY = vY

  def __str__(self):
    return '(x,y): ({},{}), (vX,vY): ({},{})'.format(self.x,self.y,self.vX,self.vY)
    