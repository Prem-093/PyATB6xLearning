#Simulate a page loading check using a while loop.
#If page_loaded becomes True within 5 seconds, print success; else timeout.
#Hint: Use a counter (like wait_time) and break condition.
#from xmlrpc.client import boolean

sec=1
while sec < 6:
    #timeout=int(input("Enter time out seconds:"))

    flag=str(input("Enter the flag:"))
    if flag =="True":
        print("Page successfully loaded within 5 sec :",flag,"Pass Attempt :",sec)
        break
    else:
        print("Page is not loaded with 5 sec :",flag,"Fail Attempt:",sec)
        sec+=1





