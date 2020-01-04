import rando
import numpy

def test_function_returns_numpy_array():
  result = rando.randomIntegerFromRange(3, 0, 50, 6)
  assert isinstance(result, numpy.ndarray)

def test_results_array_contains_given_amount_of_hits():
  result = rando.randomIntegerFromRange(3, 0, 50, 6)
  assert result.size == 6

def test_results_contain_correct_integer_values():
  result = rando.randomIntegerFromRange(3, 1, 50, 6)
  assert result.all() > 0
  assert result.all() < 51
