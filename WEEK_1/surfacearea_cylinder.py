import math
#calculate lateral surface area of cylnder
r = float(input("The radius is: "))
h = float(input("The height is: "))
pi = 22/7
lateral_surface_area = 2 * pi * r * h
total_surface_area = (2 * pi * r * r) + lateral_surface_area
print("lateral surface area of cylinder" ,lateral_surface_area)
print("total surface area of cylinder" ,total_surface_area)