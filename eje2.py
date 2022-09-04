from random import random
import matplotlib.pyplot as plt

P = [0.85, 0.07, 0.07, 0.01]
n = 100000
x = []
y = []

class Point(object):
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return '({0}, {1})'.format(self.x, self.y)

def f1(p: Point) -> Point:
  return Point(p.x*0.85 + p.y*0.04 + 0.0, p.x*-0.04 + p.y*0.85 + 1.6)

def f2(p: Point) -> Point:
  return Point(p.x*-0.15 + p.y*0.28 + 0.0,p.x*0.26 + p.y*0.24 + 0.44)

def f3(p: Point) -> Point:
  return Point(p.x*0.2 + p.y*-0.26 + 0.0, p.x*0.23 + p.y*0.22 + 1.6)

def f4(p: Point) -> Point:
  return Point(0.0, p.y*0.16)

fun = [f1, f2, f3, f4]
point = Point(0.5, 0.5)

for i in range(n):
  randomNum = random()
  x.append(point.x)
  y.append(point.y)

  if (randomNum < P[0]):
    returnFun = fun[0]
  elif (P[0] <= randomNum and randomNum < (P[0] + P[1])):
    returnFun = fun[1]
  elif ((P[0] + P[1]) <= randomNum and randomNum < (P[0] + P[1] + P[2])):
    returnFun = fun[2]
  else:
    returnFun = fun[3]

  point = returnFun(point)

plt.scatter(x, y, color='#8DD45B', marker='X', edgecolors='#8ACF5A')
plt.show()