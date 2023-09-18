# Count the number if vowels that appear in a given string


def numberOfVowels(data): 
  vowels = ["a","e","i","o","u"]
  result = 0
  for letter in data:
    if letter in vowels: # By using key word in we can check is something is contained in an array vs using array.include
      result += 1
  
  return result

print(numberOfVowels("orange"))
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))

# Create an array of vowels
# Create a result variable and set it equal to 0
# Loop through the strong provided
# Do a if statement which checks if the vowel array contains the current iteration of the loop
# If true add one to the result
# End loop and return result


