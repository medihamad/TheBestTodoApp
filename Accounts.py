account = {}
response = " "
username = " "
password = " "


print("Press 1 to create an account")
print("Press 2 to login")
response = input("Enter: ")

if response is "1":
    print("welcome to the todo list")
    print("Create an account")
    username = input("Enter username: ")
    password = input("Enter password: ")


def add_account(username, password):
    newaccount = {username: password}
    account.update(newaccount)
    return account


add_account(username, password)

print("Account created successfully")
print("Your username is " + username+" and password is " + password)
response = input("Press 1 to Login")

if response is "1":
    print("Login Page")
    username = input("Enter username: ")
    password = input("Enter password: ")

    def login(username, password):
        mytestacc = {username: password}

        for item in account.items():
            if account.items().__contains__(mytestacc.items()):
                print("welcome "+username)
        else:
            print("wrong password or username")


login(username, password)

