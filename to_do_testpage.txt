tasks = []
index = 1

rule_log = '''\n type "add" to add a task to your list
    \n type "del" to remove a task'
    \n type "view" to view your To Do List'
    \n type "done" to display your finished To Do List!'''

def addtask():
    task = input('What is your task?: ').lower()
    tasks.append(task)

    print(f"'{task}' has been added to the list")

def listtask():
    if not tasks:
        print('no tasks saved yet')
    else:
        print(f' here are your tasks:.1')
        for index, task in enumerate(tasks, start=1):
            print(f'Task {index}. {task}')


def del_task():
    listtask()
    try:
        tasktodel = int(input('Which task do you want to delete-> '))
        index + 1
        if tasktodel >= 0 and tasktodel < len(tasks):
            tasks.pop(tasktodel)
            print(f"{tasktodel} has been removed from the list")
    except:
        print('INVALID')


name = input('whats your name?: ')
print('\nHello', name.title(), " Welcome to your To Do List:")
while True:
    print(rule_log)
    action = input('\n->').split()
    if action == "add".split():
        addtask()
    elif action == 'del'.split():
        del_task()
    elif action == 'view'.split():
        listtask()
    elif action == 'done'.split(): 
        if not tasks:
            print('No tasks created')
        else:
            print('Check out your To Do List', name.title(),)
            print('-' * 30)
            print(tasks)
        break
    else:
        print('INVALID')