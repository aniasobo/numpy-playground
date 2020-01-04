from numpy.random import seed
from numpy.random import randint

def randomIntegerFromRange(num, min, max, hits): 
  seed(num)
  values = randint(min, max, hits)
  return values