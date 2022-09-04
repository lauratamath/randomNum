from random import random
import matplotlib.pyplot as plt

x = []
y = []

# p1 + p2 + p3 = 1, se asginan los distintos valores
p1 = 1/3
p2 = 1/3

class Point(object):
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return '({0}, {1})'.format(self.x, self.y)

def f1(p: Point) -> Point:
  return Point(p.x/2, p.y/2)

def f2(p: Point) -> Point:
  return Point(((p.x/2) + 0.5), p.y/2)

def f3(p: Point) -> Point:
  return Point(((p.x/2) + 0.25), ((p.y/2)+ 0.5))

point = Point(0.5, 0.5)

for i in range(1000000):
  randomNum = random()
  x.append(point.x)
  y.append(point.y)

  if (randomNum < p1):
    returnFun = f1
  elif (p1 <= randomNum and randomNum < (p2 + p1)):
    returnFun = f2
  else:
    returnFun = f3

  point = returnFun(point)

plt.scatter(x, y, color='#9ecfc2', marker='8', edgecolors='#71acaf')
plt.show()