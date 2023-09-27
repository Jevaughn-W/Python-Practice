# For the input of list, the first element should be repeated by the number of the second element

def repeatNumbers(data):
  result = []
  for array in data:
    inner_result =[]
    for i in range(array[1]):  # 
      inner_result.append(str(array[0]))
  result.append("".join(inner_result))
  return result


print(repeatNumbers([[1, 10]]))
# print(
#   repeatNumbers([
#     [1, 2],
#     [2, 3],
#   ])
# )
# print(
#   repeatNumbers([
#     [10, 4],
#     [34, 6],
#     [92, 2],
#   ])
# )

# Create a loop to loop through the list of arrays
# Create a second loop that prints the first array element the number of times for the 2n element