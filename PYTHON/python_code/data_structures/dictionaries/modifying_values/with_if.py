"""
Continuing our alien theme, let's track the position of a certain alien
that can move at different speeds. We'll store a vlaue representing the
alien's current speed then use it to determine how far to the right
the alien should move.
"""

alien_0 = {'x_position': 0,
           'y_position': 25,
           'speed': 'medium'
           }
print("Original x-position: " + str(alien_0['x_position']))

# Where we'll move the alien to the right.
# We'll implement some basic condition statments to
# figure out how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien!
    x_increment = 3

# The new position = the old position + the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
