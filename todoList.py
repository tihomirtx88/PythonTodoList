from modules.functions import get_todos, set_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S");
print("It is", now)
<<<<<<< HEAD
print("dsds")
=======
>>>>>>> e9a7905361a86e9fd5564c3f48b72197f94d524c

while True:
    user_action = input("Type add, show, exit, edit, complete: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        todos = get_todos();

        todos.append(todo + '\n')

        set_todos(todos, 'todos.txt');

    elif 'show' in user_action or 'display' in user_action:
        todos = get_todos();

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:].strip()) - 1

            todos = get_todos();

            new_todo = input("Please enter new todo: ")
            todos[number] = new_todo + '\n'

            set_todos(todos, 'todos.txt');

        except (ValueError, IndexError):
            print("Invalid number for edit.")
            continue;

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip())

            todos = get_todos();

            todos.pop(number - 1)

            set_todos(todos, 'todos.txt');
        except (ValueError, IndexError):
            print("Invalid number for complete.")
            continue;

    elif user_action.startswith("exit"):
        break

    else:
        print('Command is not valid.')

print("bye bye")