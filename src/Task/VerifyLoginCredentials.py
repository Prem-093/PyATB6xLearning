#Check if the user can log in based on correct username and password.
#I/p
#username = "admin"
#password = "1234"
#O/p
#✅ Login Successful
#For the Fail condition Other O/P = ❌ Invalid Credentials

username=str(input("Enter user name:"))
password=str(input("Enter password:"))
print(len(username))

if len(username)<=25 or len(username)>=3:
    print("✅ Valid username")
else:
    print("❌ Invalid Credentials")
if len(password)>=8 or len(password)<=16:
    if password.isalnum():
        print("✅ valid password")
        print("click on Login button")
        print("User is able to LOGIN Successfully")
    else:
        print("❌ Invalid Credentials")
        print("Please enter username and password with correct credentials")