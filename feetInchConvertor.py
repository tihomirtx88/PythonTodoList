import FreeSimpleGUI
from converters import convert

feet_label = FreeSimpleGUI.Text("Enter feet: ")
feet_input = FreeSimpleGUI.Input(key="feet")

inches_label = FreeSimpleGUI.Text("Enter inches: ")
inches_input = FreeSimpleGUI.Input(key="inches")

button = FreeSimpleGUI.Button("Convert")
output_label = FreeSimpleGUI.Text("", key="output")

window = FreeSimpleGUI.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()