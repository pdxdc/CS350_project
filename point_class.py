class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __str__(self):
    return "{}, {}".format(self.x, self.y)

  def __neg__(self):
    return Point(-self.x, -self.y)

  def __add__(self, point):
    return Point(self.x+point.x, self.y+point.y)

  def __sub__(self, point):
    return self + -point
