from Accounts import response
todo_list = []
task = ' '

def create_task(task):
    todo_list.append(task)
    print("Task has been added")


def delete_task(task=''):
    if todo_list.__contains__(task):
        todo_list.remove(task)
        print("Task has been deleted!!!")
    elif todo_list == []:
        print("there is no task in your todo list")
    else:
        print("Task not found")

def provide_option():
    print("Select options: ")
    print("1. creating a task: ")
    print("2. deleting task: ")
    print("3. deleting all task: ")
    print("4. Marking a task as finished: ")
    print("5. Exit")

def mark_as_finished(task=''):
    result = " "   
    for a in todo_list:
        if a == task:
            address_of_x = todo_list.index(a)
            address_of_x += 1
            todo_list.insert(address_of_x, '[finished]')
            print(todo_list)        
        elif a != task:
            result = "task not found"
        elif todo_list == []:
            result = "list is empty" 
        return result

def delete_all_task():
    todo_list.clear
    print("All tasks have been deleted")