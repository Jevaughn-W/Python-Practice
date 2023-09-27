# For the input of list, the first element should be repeated by the number of the second element

def repeatNumbers(data):
  result = []
  
  
  for array in data:  # Loop through array of arrays
    
    # Replicating number within the inner array
    inner_result =[]
    for i in range(array[1]):  # For loop which tells the the function how many times to repeat the number
      inner_result.append(str(array[0])) 
    result.append("".join(inner_result)) # Joins the values to the outer loop result


  return ", ".join(result)


print(repeatNumbers([[1, 10]]))
print(
  repeatNumbers([
    [1, 2],
    [2, 3],
  ])
)
print(
  repeatNumbers([
    [10, 4],
    [34, 6],
    [92, 2],
  ])
)

# Create a loop to loop through the list of arrays
# Create a second loop that prints the first array element the number of times for the 2n element