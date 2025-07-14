from modules.functions import get_todos, set_todos
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Typ in a todo");
input_box = FreeSimpleGUI.InputText(tooltip="Add to do", key="todo");
add_button = FreeSimpleGUI.Button("Add");
list_b0x = FreeSimpleGUI.Listbox(values=get_todos(),
                                 key="todos",
                                 enable_events=True,
                                 size=[45,10]);
edit_button = FreeSimpleGUI.Button("Edit");

window = FreeSimpleGUI.Window("My frist todo app",
                              layout=[[label], [input_box, add_button], [list_b0x, edit_button]],
                              font=('Helvetica', 20));
while True:
  event, values = window.read()
  match event:
      case "Add":
          todos= get_todos();
          new_todos = values['todo'] + "\n"
          todos.append(new_todos);
          set_todos(todos);
      case "Edit":
          todo_to_edit = values['todos'][0]
          new_todo = values['todo']
          # Update currentTodo
          todos = get_todos()
          index = todos.index(todo_to_edit);
          todos[index] = new_todo;
          set_todos(todos)
          # Reorder on real time
          window['todos'].update(values=todos)
      case "todos":
          # Press current value in input box
          window['todo'].update(value=values['todos'][0])
      case FreeSimpleGUI.WINDOW_CLOSED:
          break;

window.close();
