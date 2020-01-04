from test.rando import randomIntegerFromRange

def initial_user_menu():
  print("This pseudorandom number generator requires the following arguments:")
  print("1. the seed as an integer")
  print("2. the range - minimum and maximum values (inc)")
  print("3. number of results")
  print("Do you have those values ready? y/n")

initial_user_menu()
# capture stdout
# pretty print the returned list