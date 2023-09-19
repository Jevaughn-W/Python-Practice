# Given an list of dictionary containing instructors, identify the instructor with the longest name

def instructorWithLongestName(instructors):
  # Put your solution here
  return None

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