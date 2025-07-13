from modules.functions import get_todos, set_todos
import FreeSimpleGUI

label = FreeSimpleGUI.Text("Typ in a todo");
input_box = FreeSimpleGUI.InputText(tooltip="Add to do", key="todo");
add_button = FreeSimpleGUI.Button("Add");

window = FreeSimpleGUI.Window("My frist todo app",
                              layout=[[label], [input_box, add_button]],
                              font=('Helvetica', 20));
while True:
  event, values = window.read()
  match event:
      case "Add":
          todos= get_todos();
          new_todos = values['todo'] + "\n"
          todos.append(new_todos);
          set_todos(todos);
      case FreeSimpleGUI.WINDOW_CLOSED:
          break;
window.close()
