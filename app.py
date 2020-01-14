from numpy.random import seed
from numpy.random import randint

def randomIntegerFromRange(num, min, max, hits): 
  seed(num)
  values = randint(min, max, hits)
  return values

def initial_user_menu():
  print('This pseudorandom number generator requires the following arguments:')
  print('1. the seed as an integer')
  print('2. the range - minimum and maximum values (inc)')
  print('3. number of results')
  print('Do you have those values ready? y/n')

def ready_to_choose():
  print('please choose your values in this order, divided by a single space:')
  print('seed minimum_value maximum_value number_of_results')
  print('all values must be integers')

def breakout_menu():
  print('Press any button to exit.')

while True:
  initial_user_menu()
  choice = input()

  if choice == 'y':
    ready_to_choose()
    chosen_values = input()

  else:
    breakout_menu()
    any_button = input()

    if any_button != null:
      break
