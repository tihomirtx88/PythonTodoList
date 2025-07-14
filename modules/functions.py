def get_todos():
    """Read a text file and return to list of todo items"""
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local;

def set_todos(todos_arg, filepath = 'todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)