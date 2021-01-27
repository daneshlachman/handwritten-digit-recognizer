import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Draw something')],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Handwritten digit predicter', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()