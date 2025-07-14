from modules.functions import get_todos, set_todos
import FreeSimpleGUI
import time

FreeSimpleGUI.theme("Black")

clock = FreeSimpleGUI.Text("", key="clock");
label = FreeSimpleGUI.Text("Typ in a todo");
input_box = FreeSimpleGUI.InputText(tooltip="Add to do", key="todo");
add_button = FreeSimpleGUI.Button("Add");
list_b0x = FreeSimpleGUI.Listbox(values=get_todos(),
                                 key="todos",
                                 enable_events=True,
                                 size=[45,10]);
edit_button = FreeSimpleGUI.Button("Edit");

complete_button = FreeSimpleGUI.Button("Complete");

exit_button = FreeSimpleGUI.Button("Exit");

window = FreeSimpleGUI.Window("My frist todo app",
                              layout=[[clock],
                                      [label],
                                      [input_box, add_button],
                                      [list_b0x, edit_button, complete_button],
                                      [exit_button]],
                              font=('Helvetica', 20));
while True:
  event, values = window.read(timeout=200)
  window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
  match event:
      case "Add":
          todos= get_todos();
          new_todos = values['todo'] + "\n"
          todos.append(new_todos);
          set_todos(todos);
          window['todos'].update(values=todos)
      case "Edit":
          try:
              todo_to_edit = values['todos'][0]
              new_todo = values['todo']
              # Update currentTodo
              todos = get_todos()
              index = todos.index(todo_to_edit);
              todos[index] = new_todo;
              set_todos(todos)
              # Reorder on real time
              window['todos'].update(values=todos)
          except IndexError:
              FreeSimpleGUI.popup("Please select an item first", font=("Helvetica",20))

      case "Complete":
          # Complete logic implementation
          try:
              todo_to_complete = values["todos"][0]
              todos = get_todos()
              todos.remove(todo_to_complete)
              set_todos(todos)
              window['todos'].update(values=todos)
              window['todo'].update(value="")
          except IndexError:
              FreeSimpleGUI.popup("Please select an item to complete", font=("Helvetica",20))
      case "todos":
          # Press current value in input box
          window['todo'].update(value=values['todos'][0])
      case "Exit":
          break;
      case FreeSimpleGUI.WINDOW_CLOSED:
          break;

window.close();
