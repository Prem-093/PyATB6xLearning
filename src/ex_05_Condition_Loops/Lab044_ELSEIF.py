# Find the positive number is even or odd

num=int(input("enter num:"))
if num<=0:
    print("Enter a valid number")
else:
    if num%2==0:
        print("Num is even",num)
    else:
        print("Num is odd",num)

