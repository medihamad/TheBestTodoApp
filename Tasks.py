todo_list = []


def create_task(task=''):
    todo_list.append(task)


create_task('medi')
create_task("hamad")



# def delete_task(task=''):

#    if todo_list.__contains__(task):
#        todo_list.remove(task)


#delete_task('medi')


def mark_as_finished(task=''):

    for x in todo_list:
        if x is task:
            address_of_x = todo_list.index(task)
            print(address_of_x)
            address_of_x += 1
            todo_list.insert(address_of_x, '[finished]')
            break


mark_as_finished("hamad")

mark_as_finished("medi")

print(todo_list)