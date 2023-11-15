
def funLogger(fnc):

    def helper(amount):
        print("Logging into a service......")
        # print(f"Greetings {gname}")
        fnc(amount)
        print("Logging out of the service....")
        print("-" * 60)

    return helper

@funLogger              # deposit = funLogger(deposit)
def deposit(amt):
    print(f"Amount of {amt} credited into the account......")


@funLogger
def withdraw(amt):
    print(f"Amount {amt} debitted from the account.......")


deposit(25000)
withdraw(10000)
