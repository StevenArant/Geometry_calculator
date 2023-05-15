# Geometry_functions.py
# New custom module to hold geometry calculations.
import math
pi: float = math.pi


# --------- 2d Functions ----------

# Square area function
def square_area():
    userinput = float(input("Enter a side measurement for the area of a square: "))
    x: float = float(pow(userinput, 2))
    print("The area of the square is: {}".format(x))


# Rectangle area function
def rectangle_area():
    length = float(input("Enter the length measurement: "))
    width = float(input("Enter the width measurement: "))
    x = float(length * width)
    print("The area of the rectangle is: {}".format(x))


# Square triangle area function
def sqtriangle_area():
    userinput = float(input("Enter a side measurement for the area of a square triangle: "))
    x = float(pow(userinput, 2) / 2)
    print("The area of the square is: {}".format(x))

# Circle area function
def circle_area():
    print("Do you want to solve with:\n1. Radius\n2. Diameter\n3. Circumference")
    userinput = input("Enter selection: ")
    if userinput == "1":
        userinput = float(input("Enter the radius of the circle: "))
        x = pi * float(pow(userinput, 2))
        print("The area of the circle is: {}".format(x))
    if userinput == "2":
        userinput = float(input("Enter the diameter of the circle: "))
        x = (pi / 4) * pow(userinput, 2)
        print("The area of the circle is: {}".format(x))
    if userinput == "3":
        userinput = float(input("Enter the circumference of the circle: "))
        x = pow(userinput, 2) / (4 * pi)
        print("The area of the circle is: {}".format(x))


# --------- 3d Functions ----------

# Cube volume function
def cube_volume():
    userinput = float(input("Enter a side measurement for the volume of a cube: "))
    x = float(pow(userinput, 3))
    print("The volume of the cube is: {}".format(x))

# Rectangular Prism volume function
def rectangular_volume():
    length = float(input("Enter the length measurement: "))
    height = float(input("Enter the height measurement: "))
    width = float(input("Enter the width measurement: "))
    x = float(length * height * width)
    print("The volume of the rectangular prism is: {}".format(x))

# Square Pyramid volume function
def sqpyramid_volume():
    base_length = float(input("Enter the base length: "))
    base_width = float(input("Enter the base width: "))
    base_area = float(base_length * base_width)
    height = float(input("Enter the height: "))
    x = (1 / 3) * base_area * height
    print("The volume of the pyramid is: {}".format(x))
