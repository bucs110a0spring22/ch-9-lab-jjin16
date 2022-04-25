class Rectangle:
  def __init__(self,x,y,height,width):
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
    info_string=f"(x : {self.x}, y: {self.y}) width: {self.width}, height: {self.height}"
    return info_string