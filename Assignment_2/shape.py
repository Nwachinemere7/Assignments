# ## 12.

# Write a program that determines the name of a shape from its number of sides. 
# Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. 
# If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

#Solution:
polygons = {3: 'Triangle', 4: 'Square', 5: 'Pentagon', 6: 'Hexagon', 7: 'Heptagon', 8: 'Octagon', 9: 'Nonagon', 10: 'Decagon'}

num_sides = int(input("Enter the number of sides of the shape: "))
for x in polygons.keys():
    if num_sides == x:
        print(polygons.get(x))