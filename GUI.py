import Function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a Todo")
add_button = sg.Button("Add")


window = sg.Window(' My Trajectory App', layout=[[label], [input_box, add_button]])
window.read()
window.close()