# Initialize offset
offset = -6
# While loop
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else : 
      offset += 1   
    print(offset)
# correcting...
# -5
# correcting...
# -4
# correcting...
# -3
# correcting...
# -2
# correcting...
# -1
# correcting...
# 0

# for loop
# enumerate: generate index and value pair, so that we can access index as well
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)
# 11.25
# 18.0
# 20.0
# 10.75
# 9.5

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room "+str(index + 1)+": "+str(area))
# room 1: 9.5
# room 2: 9.5
# room 3: 9.5
# room 4: 9.5
# room 5: 9.5

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for row in house:
    print("the "+str(row[0])+" is "+str(row[1])+" sqm")
# the hallway is 11.25 sqm
# the kitchen is 18.0 sqm
# the living room is 20.0 sqm
# the bedroom is 10.75 sqm
# the bathroom is 9.5 sqm