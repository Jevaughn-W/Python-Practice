# Create a function that takes in 2 arguments, a list of strings and a decimal. The function assess the count of dirty and clean and check that the % of dirty is less than the threshold of the second argument

def checkAir(samples, threshold):
  #Code here!
  return None

print(checkAir(
  ['clean', 'clean', 'dirty', 'clean', 'dirty', 'clean', 'clean', 'dirty', 'clean', 'dirty'],
  0.3
))

print(checkAir(
  ['dirty', 'dirty', 'dirty', 'dirty', 'clean'],
  0.25
))

print(checkAir(
  ['clean', 'dirty', 'clean', 'dirty', 'clean', 'dirty', 'clean'],
  0.9
))