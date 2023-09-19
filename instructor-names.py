# Given an list of dictionary containing instructors, identify the instructor with the longest name

def instructorWithLongestName(instructors):
  result = 0
  for instructor in instructors:
    if len(instructor["name"]) > result:
      result = len(instructor["name"])

  return result

print(
  instructorWithLongestName([
    { "name": "Samuel", "course": "iOS" },
    { "name": "Jeremiah", "course": "Web" }, # Note that when it comes to creating JS objects - it is the same step except that the key needs to be encased in quotes. Dictionaries (objects) can also be created using the dict() function see https://realpython.com/python-dicts/ 
    { "name": "Ophilia", "course": "Web" },
    { "name": "Donald", "course": "Web" },
  ])
)
print(
  instructorWithLongestName([
    { "name": "Matthew", "course": "Web" },
    { "name": "David", "course": "iOS" },
    { "name": "Domascus", "course": "Web" },
  ])
)

# Create a variable to count the size of the instructor name
# Use a for loop to iterate through the array of objects
# Use the key value to acess the name and check the length of the string using the Len function
# If the value is larger that the value in the counter replace it
# At the end of the loop return the the count