# Given a normal string of words, replace all the white space with %20


def urlEncode(text):
  result = []


  for char in text.strip():  # Built in python trim spaces - maybe could try to implement in a refactor
    if char == " ":
      result.append("%20")
    else:
      result.append(char)
  return "".join(result) # Function that join the list is no spaces or characters


print(urlEncode("Lighthouse Labs"))
print(urlEncode(" Lighthouse Labs "))
print(urlEncode("blue is greener than purple for sure"))


# Create a results array
# Loop through the string using for in
# Trim the outer spaces of the array
# Check in the value is a space - if it is a space append %20 to the result array otherwise append the letter
# At the end of the for loop collapse the array and return the result