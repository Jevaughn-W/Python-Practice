#Creating a function which adds numbers based on the condition (odd or even) when passed in


def conditionalSum(values, condition):
  results = [] # Container for the values which will be added
  if condition == "even": # Check for the condition before applying the for loop - reduces the number of lines needed
    for i in values:
      if i % 2 == 0:
        results.append(i)
    return sum(results) #Utilizing sum function in python for symplicity
  else:
    for i in values:
      if i % 2 > 0:
        results.append(i) # Equivalent to array.push()
    return sum(results)



print(conditionalSum([1, 2, 3, 4, 5], "even"))
print(conditionalSum([1, 2, 3, 4, 5], "odd"))
print(conditionalSum([13, 88, 12, 44, 99], "even"))
print(conditionalSum([], "odd"))


# Create result array
# Loop through the array proviced
# Check the which condition is applicable
# Look at condition and push all the values to the results if meets the criteria
# Use something to sum the result array