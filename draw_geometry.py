# experimental function to draw a square in the terminal.
# I want to add numbers to specific places to more accurately show the dimensions, etc.

# --------- 2d Functions ----------

# Draws a simple square in the terminal
def draw_square():
    # To-Do: Add visual measurements to the sides
    print("# " * 10), print(("# " + (" " * 15) + " #\n") * 5, end=""), print("# " * 10)


# Draws a simple rectangle in the terminal
def draw_rectangle():
    print("# " * 15), print(("# " + (" " * 25) + " #\n") * 5, end=""), print("# " * 15)


# Draws a simple triangle in the terminal
def draw_triangle():
    print(str.center("#", 16," "))
    print(str.center("# #", 16," "))
    print(str.center("#   #", 16," "))
    print(str.center("#     #", 16," "))
    print(str.center("#       #", 16," "))
    print(str.center("#         #", 16," "))
    print(str.center("#           #", 16," "))
    print("#" * 15)

# Draws a simple circle in the terminal
def draw_circle():
    pass

# --------- 3d Functions ----------

# Draws a simple cube in the terminal
def draw_cube():
    pass

# Draws a simple rectangular prism in the terminal
def draw_prism
    pass