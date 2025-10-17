# Problem to find the max between two.

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

num1=int(input("Enter frst num:"))
num2=int(input("Enter second num:"))

if num1<=0 or num2<=0:
    print("Enter valid numbers")
else:
    if num1>num2:
        print("num1 is greater")
    else:
        print("num2 is greater")