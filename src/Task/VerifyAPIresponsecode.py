#You receive an API response code from your test script.
#Write an if-else block to check whether the response is successful (status code 200) or not.
from contextlib import nullcontext
from tokenize import String

#I/P response = 404 , O/P ❌ Failed API Request
#I/P response = 200 , O/P ✅ Passed API Request

url=str(input("Enter the URL:").strip())
getResponseCode=int(input("Get response code:").strip())
if url!= nullcontext:
    print("valid url")
    if getResponseCode==200:
        print("API request PASS ✅")
    elif getResponseCode==404:
        print("API request Fail ❌")
    else:
        print("Response code of API request need to check")





