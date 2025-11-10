def validate_status_code(Statuscode):
    if Statuscode > 0:
        if Statuscode==200:
            print("Statuscode 200 API request pass")
        else:
            print("Statuscode is not 200 , API request Fail")
    else:
        print("Status code is Invalid")

#validate_status_code(400)
#validate_status_code(300)
#validate_status_code(Statuscode=200)
#validate_status_code(-1)

validate_status_code(input("Enter your status code"))

