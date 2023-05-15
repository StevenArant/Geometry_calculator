# Geometry Calculator
# This script is meant to process geometry calculations.

# Calculations included:
# Square area, Rectangle area, Triangle area, Circle area
# Cube area, Rectangular Prism area, Pyramid area
#
# Calculations to add:
# Sphere area, Cylinder area

import Geometry_functions
import draw_geometry

while True:

    # Initial prompt to ask what to calculate.
    prompt1 = (input("2d or 3d: "))

    # -------------------- 2d shape areas --------------------
    if prompt1 == "2d":

        # Initial 2d prompt and choices
        print()
        print("What would you like to calculate?")
        print("1. Square Area\n2. Rectangle Area\n3. Triangle Area\n4. Circle Area")
        prompt2 = input("Enter selection: ")

        # Square area calculation
        if prompt2 == "1":
            print()
            print("You've selected Square.")
            print()
            draw_geometry.draw_square()
            print()
            Geometry_functions.square_area()
            print("-" * 50)

        # Rectangle area calculation
        elif prompt2 == "2":
            print()
            print("You've selected Rectangle.")
            print()
            draw_geometry.draw_rectangle()
            print()
            Geometry_functions.rectangle_area()
            print("-" * 50)

        # Square triangle area calculation
        elif prompt2 == "3":
            print()
            print("You've selected Square Triangle.")
            print()
            draw_geometry.draw_triangle()
            print()
            Geometry_functions.sqtriangle_area()
            print("-" * 50)

        elif prompt2 == "4":
            print()
            print("You've selected Circle.")
            print()
            Geometry_functions.circle_area()
            print("-" * 50)

    # -------------------- 3D shape volumes --------------------
    elif prompt1 == "3d":

        # Prompt for type of 3d calculation
        print()
        print("You've selected volume.\nWhat would you like to calculate?")
        print("1. Cube\n2. Rectangular Prism\n3. Pyramid")
        prompt2 = input("Enter selection: ")

        # Cube area calculation
        if prompt2 == "1":
            print()
            print("You've selected Cube.")
            print()
            Geometry_functions.cube_volume()
            print("-" * 50)

        # Rectangular area calculation
        elif prompt2 == "2":
            print()
            print("You've selected Rectangular Prism.")
            print()
            Geometry_functions.rectangular_volume()
            print("-" * 50)

        # Pyramid volume calculation
        elif prompt2 == "3":
            print()
            print("You've selected Pyramid.")
            print()
            Geometry_functions.sqpyramid_volume()
            print("-" * 50)

    elif prompt1 == "exit" or "q":
        break

    # Prints invalid input box and returns to beginning of loop.
    else:
        print("-" * 50)
        print("-"*17, "Invalid input.", "-"*17)
        print("-" * 50)