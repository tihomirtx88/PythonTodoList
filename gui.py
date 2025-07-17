from modules.functions import get_todos, set_todos
import FreeSimpleGUI
import time
from zip_extractor import extract_archive

FreeSimpleGUI.theme("Black")

clock = FreeSimpleGUI.Text("", key="clock");
label = FreeSimpleGUI.Text("Typ in a todo");
input_box = FreeSimpleGUI.InputText(tooltip="Enter todo", key="todo");

add_button = FreeSimpleGUI.Button(size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add todo", key="Add");
list_b0x = FreeSimpleGUI.Listbox(values=get_todos(),
                                 key="todos",
                                 enable_events=True,
                                 size=[45,10]);
edit_button = FreeSimpleGUI.Button("Edit");

label_archive = FreeSimpleGUI.Text("Select archive");
archive_input = FreeSimpleGUI.Input();
choose_button1 = FreeSimpleGUI.FileBrowse("Choose", key="archive")

label_folder = FreeSimpleGUI.Text("Select dest dir");
folder_input = FreeSimpleGUI.Input();
choose_button2 = FreeSimpleGUI.FileBrowse("Choose", key="folder")

extract_button = FreeSimpleGUI.Button("Extract")
output_label = FreeSimpleGUI.Text(key="output", text_color="green");

complete_button = FreeSimpleGUI.Button("Complete");

exit_button = FreeSimpleGUI.Button("Exit");

window = FreeSimpleGUI.Window("My frist todo app",
                              layout=[[clock],
                                      [label],
                                      [input_box, add_button],
                                      [list_b0x, edit_button, complete_button],
                                      [exit_button],
                                      [label_archive,archive_input,choose_button1],
                                      [label_folder, folder_input, choose_button2],
                                      [extract_button, output_label]],
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
      case "Extract":
          try:
              archivepath = values["archive"]
              dest_dir = values["folder"]
              extract_archive(archivepath, dest_dir)
              window["output"].update(value="Extraction complete")
          except Exception as e:
              window["output"].update(value=f"Error: {e}")
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
