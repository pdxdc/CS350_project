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



a = Point(5,3)
b = Point(7,7)
c = Point(25,33)

point_list_ = [a,b,c]

def quickhull(point_list):
	
	for i in point_list:
		print "x = ", i.x, "  y = ", i.y
	
	return

quickhull(point_list_)
#print c.x
#print a.y
#print b+b
