# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
# i/p - r - float
# o/p  -> string formatted output of area.

import math
pie=input("Enter the value of pi :")
pi=float(pie)
radius=input("Enter the value of radius:")
r=float(radius)
Area=pi*r**r
print("area of circle :", Area)
# String data formatting , Python f-strings, formatted string literals
print(f"Area of the circle is -> {Area:.2f}")

