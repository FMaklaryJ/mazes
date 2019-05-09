This is a fun little waste of time I made.
Requires matplotlib, math, and numpy.

Maze 2.py and Maze 3.py will solve a maze through 2 different methods.
They take in a .png image of a maze, start at the blue dot (0,0,255 in RGB color),
and end at the red dot (255,0,0), and take paths along the black lines (0,0,0).
They have stepsize of 1 pixel.

Simply put, maze 2.py picks its turns randomly and tries to find the shortest path,
counting the dead ends it runs into, and maze 3.py starts over at each dead end,
but blocks off the way to the dead end.

You run it, write the name of the picture (with .png at the end), 
tell it how many times it should run, and then tadaa, it hopefully found a path.
Hope you have fun with it.