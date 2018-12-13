class Cart:
  def __init__(self,x,y,axis,direc):
    self.x = x
    self.y = y
    self.axis = axis
    self.direc = direc
    self.state = 0
  
  def __str__(self):
    return '(x,y) direction: ({},{}) {} {}'.format(self.x, self.y, self.direc, self.axis)
  
  def __lt__(self,other):
    return self.y < other.y or (self.y == other.y and self.x < other.x)

  def move(self):
    if(self.axis == 'x'):
      self.x += self.direc
    else:
      self.y += self.direc
      
  def turnLeft(self):
    if(self.axis == 'x'):
      self.direc = -self.direc
    self.turn()
  
  def turnRight(self):
    if(self.axis == 'y'):
      self.direc = -self.direc
    self.turn()

  def intersec(self):
    if(self.state == 0):
      self.turnLeft()
    elif(self.state == 2):
      self.turnRight()
    self.state += 1
    self.state %= 3
  
  def turn(self):
    if self.axis == 'x':
      self.axis = 'y'
    elif self.axis == 'y':
      self.axis = 'x'

class Track:
  def __init__(self,x,y,pic):
    self.x = x
    self.y = y
    self.pic = pic

    self.full = False
  
  def __str__(self):
    return self.pic