#Timothy Sawyer, this is my To-Do List application project made in python
#it has 3 functons for Adding, Deleting, & Viewing the To-DO list
#the To-Do List runs in a while true loop that breaks when done is selected.
tasks = []


rule_log = '''\n type "add" to add a task to your To Do list
    \n type "del" to remove a task from your To Do List'
    \n type "view" to view your To Do List'
    \n type "done" to display your finished To Do List!'''
#rule log prints at the top of thw while loop to keep the rules displayed
def addtask():
    task = input('What is your task?: ').lower()
    tasks.append(task)
    print(f"'{task}' has been added to the list")
#function to add task
def listtask():
        print(f'here are your tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'Task {index}. {task}'.title())
#function to list task, for loop to remove zero from the list
def del_task():
    listtask()
    tasktodel = int(input('Which task do you want to delete-> '))
    up_tasktodel = int(tasktodel - 1)#-1 corrects the selection to match the task index
    rem_task = tasks.pop(up_tasktodel)
    print(f"{rem_task} has been removed from the list")
#del task function tied in with the list task function


name = input('TO CREATE A TO DO LIST PLEASE ENTER YOUR NAME: ')
print('\nHello', name.title(), " Welcome to your To Do List:")
while True:
    try:
        print(rule_log)
        action = input('\n->').split()
        if action == "add".split():
            addtask()
        elif action == 'del'.split():
                if len(tasks) <= 0:
                    print('No Task Created')
                else:
                    try:
                        del_task()
                    except IndexError:
                        print('NOT A VALID TASK NUMBER')
        elif action == 'view'.split():
            try: 
                if len(tasks) <= 0:
                    print('No Task Created')
                else:
                    listtask()
            except ValueError:
                print('Invalid Input')
        elif action == 'done'.split(): 
            if not tasks:
                print('No tasks created')
            else:
                print('Check out your To Do List', name.title(),)
                print('-' * 30)
                listtask()
            break
        else:
            print('NOT A OPTION')
    except ValueError:
        print('INVALID INPUT')
#this code block operates the functions and loops until done is selected