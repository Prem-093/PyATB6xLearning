#In automation, you often compare expected and actual outputs.
#Write code to check if a test case passed or failed.
#expected_title = "Dashboard"
#actual_title = "Dashboard "
#✅ Test Passed – Title matches
#True - why >  Strip and convert them into the lowercase = both of them are equal

expected_Title=str(input("Enter expected Title").strip())
Actual_Title=str(input("Enter actual Title").strip())

if expected_Title==Actual_Title:
    print("✅ Test Passed – Title matches")
else:
    print("❌ Test Fail - Title not matches")