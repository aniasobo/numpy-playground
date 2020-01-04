import rando
import numpy

def test_randomIntegerFromRange():
  result = rando.randomIntegerFromRange(3, 0, 50, 6)
  print(result)
  assert isinstance(result, numpy.ndarray)