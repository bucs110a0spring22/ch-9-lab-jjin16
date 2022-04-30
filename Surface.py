from Rectangle import Rectangle
class Surface:
  def __init__(self, filename, x, y, height, width):
    """
    Sets up the instance variable for rectangle object
    Args:(string)filename, (integer)x, (integer)y, (integer)height, (integer)width
    return: none
    """
    self.rect=Rectangle(x,y,height,width)
    self.image=str(filename)
  def getRect(self):
    """
    returns the filename parameter of the surface object 
    Args: none
    return:(string) The filename parameter representing the file path
    """
    return self.rect