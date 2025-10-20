count=1
while count<4:
    res_code=int(input("Enter thr response code: "))
    print(res_code,"Attempt:",count)
    if res_code==200:
        print("\n ✅ Test Passed",count)
        break
    else:
        print("Attempt:",count,"Test Failed")

    count+=1
