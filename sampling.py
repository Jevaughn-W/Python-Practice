# Create a function that takes in 2 arguments, a list of strings and a decimal. The function assess the count of dirty and clean and check that the % of dirty is less than the threshold of the second argument

def checkAir(samples, threshold):
  
  counter = 0 # Variable to keep track of the count of dirty sample
  
  for sample in samples: # Looper
    if sample == "dirty":
      counter += 1 
  if (counter / len(samples)) > threshold :
    return "Polluted"
  else:
    return "Clean"

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

# Create a counter variable = 0
# Take in list and traverse using for loop
# For each element, check if there are any diry, if yes add one to counter
# At the end of the loop check if the count divided by the list length is greater than the threshold
# If yes return polluted else return clean