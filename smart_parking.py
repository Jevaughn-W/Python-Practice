# returns the coordinates of an available parking spot for the vehicle, or returns false if there is no available spot

def whereCanIPark(spots, vehicle):
  # Loop outer array
  # Loop inner array
  # Check if letter is capitalized
  # If yes check if 

  x_coordinate = 0
  y_coordinate = 0

  keys = { # Created a dictionary that contains the vehicles allowed in each parking
    "S" : ["small", "motorcycle"],
    "R" : ["small", "regular", "motorcycle"],
    "M": ["motorcycle"] 
  }

  for spot in spots:
    for space in spot:
      if space.isupper() and vehicle in keys[space]: #identifying the letters are capitalized and checking if the vehicle is within the letter
        return [x_coordinate ,y_coordinate] # Returns the array
      x_coordinate += 1 # Adds 1 to the x-coordinate if there isn't anything found
    x_coordinate = 0 # Need to reset the x-coordinate to zero for each new row
    y_coordinate += 1 # Adds 1 to the y-cordinate if there isn't anything found in the entire row

  return False

print(whereCanIPark(
  [
    # COLUMNS ARE X
    # 0    1    2    3    4    5
    ['s', 's', 's', 'S', 'R', 'M'], # 0 ROWS ARE Y
    ['s', 'M', 's', 'S', 'r', 'M'], # 1
    ['s', 'M', 's', 'S', 'r', 'm'], # 2
    ['S', 'r', 's', 'm', 'r', 'M'], # 3
    ['S', 'r', 's', 'm', 'r', 'M'], # 4
    ['S', 'r', 'S', 'M', 'M', 'S']  # 5
  ],
  'regular'
))

print(whereCanIPark(
  [
    ['M', 'M', 'M', 'M'],
    ['M', 's', 'M', 'M'],
    ['M', 'M', 'M', 'M'],
    ['M', 'M', 'r', 'M']
  ],
  'small'
))

print(whereCanIPark(
  [
    ['s', 's', 's', 's', 's', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['s', 'm', 's', 'S', 'r', 's'],
    ['S', 'r', 's', 'm', 'r', 's'],
    ['S', 'r', 's', 'm', 'R', 's'],
    ['S', 'r', 'S', 'M', 'm', 'S']
  ],
  'motorcycle'
))