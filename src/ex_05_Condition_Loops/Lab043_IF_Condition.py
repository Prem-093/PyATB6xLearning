# Write a program to take a user age and
# let him know if he can go the club.
# 21
# Logic Building Formula

# Step 1
# i/p - age, int
# o / p - String (reuslt -> Can go to club or not.


age=int(input("Enter age :"))



if(age<=0 or age>122):
    print("age must be between 0 and 122")

else:
    if age>=21:
        print("Eligible for going to club")
    else:
        print("Eligible for going to club ")

    # Step 4.  Check for the edge cases.
    # We should consider edge cases such as:
    # Negative ages or extremely high values -> program will break.
    # Non-numeric input - ABC
    # Age which is valid. > 130

    # Step 5.  Optimize the code.
    # Handle all the edges.