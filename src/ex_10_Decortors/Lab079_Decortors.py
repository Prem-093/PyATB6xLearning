def add_security(func):

    def wrapper():
        print("Add halmet,gloves,knee guard,back camera")
        print("OTP should be asked from rental car driver")
        func()
        print("Secure Driving, Leave all the items")
        print("Secure Driving, Leave the passenger at spot safely")

    return wrapper()


@add_security
def ola_scooter():
    print("I am driving OLA scooter")

@add_security
def rental_cabs():
    print("Rental Cabs")
