
account = {}
response = " "
name = " "
password = " "


def add_account(name, password):
    name = name
    password = password
    user = {name :name, password:password}
    account[name] = user 
    print("Account created successfully!!!")
    return True


def login(name, password):
   name = input("Enter your username: ")
   password = input("Enter your password: ") 
   if account[name]:
       print("Your username is "+ name)
       return True
   else:
       print("Wrong password or Username")
       return False
        
