class Rectangle:
  def __init__(self,x,y,height,width):
    """
    Sets up the instance variable for rectangle object
    Args:(integer)x, (integer)y, (integer)height, (integer)width
    return: none
    """
    if x<0:
      x=0
    if y<0:
      y=0
    if height<0:
      height=0
    if width<0:
      width=0
    self.x=x
    self.y=y
    self.height=height
    self.width=width
  def __str__(self):
    """
    Stores the parameters of rectangle object into info_string and returns it.
    Args: none
    Return:(string) the values for rectangle parameters
    """
    info_string=f"(x : {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"
    return info_string