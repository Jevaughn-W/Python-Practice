def sumLargestNumbers(data):
  largest = 0
  second_largest = 0

  # Finding largest
  for i in data:
    if i > largest:
      largest = i
  
  # Finding second largest
  for j in data:
    if largest > j > second_largest:
      second_largest = j
  
  return largest + second_largest


print(sumLargestNumbers([1, 10]))
print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))



# First interate through the list of numbers
# Find the max value of the list and save it
# Remove the max value from the list
# Repeat steps 1 and 2