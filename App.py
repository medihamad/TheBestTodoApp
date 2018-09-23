from Accounts import account, response, name, password, add_account, login
from Tasks import todo_list, create_task, task, delete_task, task, delete_all_task, mark_as_finished, provide_option
x = True

if __name__ == "__main__":

    print("Welcome to the todo list: ")
    print("Press 1 for creating an account")
    print("Press 2 for login")
    response = input("Enter your choice: ")

    if response == "1":
        print("Create your account: ")
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        add_account(name, password)

    elif response == "2":
        print("Login: ")
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        if todo_list == []:
            print("Please create account first")
            name = input("Enter your username: ")
            password = input("Enter your password: ")
            add_account(name, password)
            
    while x is True:
        provide_option()        
        response = input("Enter your choice: ")

        if response == "1":
            response = input("create task: ")
            create_task(response)
        elif response == "2":
            print(todo_list)
            response = input("Enter task you want to delete")
            delete_task(response)
            print(todo_list)
        elif response == "3":
            print(todo_list)
            delete_all_task()
            print(todo_list)
        elif response == "4":
            print(todo_list)
            response = input("Mark a task as finished: ")
            mark_as_finished(response)
        elif response == "5":
            break
        else:
            print("Invalid response")


# print("Press 1 to create an account")
# print("Press 2 to login")
# response = input("Enter your choice: ")

# while response == "2":
#     print("no accountm please create one: ")
#     response = input("Do you wish to continue?(y/n): ")


# while response == "1":
#     print("welcome to the todo list")
#     print("Create an account")
#     add_account(username, password)
#     response = input("Do you wish to login?(y/n): ")
    
#     if response == 'y':
#         login(username, password)
               
# provide_option()
# response = input("Enter your choice: ")

# while x == True:   
#     if response == "1":
#         task = input("create task: ")
#         create_task(task)
#         response = input("Do you wish to continue?(y/n): ")
#         if response == 'y':
#             provide_option()
#             response = input("Enter your choice: ")
#     elif response == "2":
#         task = input("Enter task you wish to delete: ")
#         delete_task(task)
#         response = input("Do you wish to continue?(y/n): ")
#         provide_option()
#         response = input("Enter your choice: ") 
#     elif response == "3":
#         delete_all_task()
#         response = input("Do you wish to continue?(y/n): ")
#         provide_option()
#         response = input("Enter your choice: ") 
#     elif response == "4":
#         print(todo_list)
#         task = input("Enter task already finished: ")
#         mark_as_finished(task)
#         print(result)
#         response = input("Do you wish to continue?(y/n): ")
#         provide_option()
#         response = input("Enter your choice: ") 
#     elif response == "n":
#         break
#     else:
#         print("Invalid input")
#         response = input("Do you wish to continue?(y/n): ")
#         provide_option()
#         response = input("Enter your choice: ")     
   
             