import PySimpleGUI as sg

layout = [[sg.Text('Enter Value:')],
          [sg.Input(do_not_clear=False), sg.T('Not Selected ', size=(52,1), justification='left',text_color='red', background_color='white', key='_USERNAME_')],
          [sg.Button('Enter'), sg.Exit()],
          [sg.Text('List Of Values:')],
          [sg.Listbox(values=('value1', 'value2', 'value3'), size=(30, 2), key='_LISTBOX_')]]

window = sg.Window('My Application', layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Enter':
        window.Element('_LISTBOX_').Update(values=[event, values, 'new value 3'])
        #window.FindElement('_USERNAME_').Update(values[0])
window.Close()