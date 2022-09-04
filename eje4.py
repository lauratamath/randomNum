# Implementation based on example provided by Saika Tsahana: https://www.geeksforgeeks.org/monte-carlo-integration-in-python/

from scipy import random
import numpy as np
import math

aLim = 0
bLim = 1
n = 100

# Create function
def mainFunc(x):
  return 2 * math.exp(-math.pow((1/x - 1), 2)) / math.pow(x, 2)

while n <= 100000:
  # Create collection of pseudo random numbers
  uniformRandom = np.zeros(n)

  # Populate collection with uniform random numbers
  for i in range(len(uniformRandom)):
    uniformRandom[i] = random.uniform(aLim, bLim)

  integralSum = 0.0

  for num in uniformRandom:
    integralSum += mainFunc(num)

  result = (bLim - aLim) / float(n) * integralSum

  print("Monte Carlo Approximation with n =", n)
  print(result)

  if n == 100:
    n = 10000
  elif n == 10000:
    n = 100000
  elif n == 100000:
    n += 1