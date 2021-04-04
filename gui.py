import PySimpleGUI as sg
import scraper as Scraper

layout = [  [sg.Text('URL'), sg.Input(key='url')],
            [sg.Text('Shoepalace'), sg.Button('spVariants'), sg.Button('spStock') ],
            [sg.Text('ShopNiceKicks'), sg.Button('snkVariants')] ]

window = sg.Window('Jill\'s scraper',
                   layout,
                   resizable=True,
                   finalize=True)  # this is the chang

window.set_min_size((600,400))

window.bind('<Configure>',"Event")

while True:
    event, values = window.read()
    if event == 'spVariants':
        data = Scraper.scrapeShoePalanceWebsite(values['url'])
        Scraper.spVariants(data)
        print('clicked spVariants')

    if event == 'spStock':
        print('clicked spStock')

    if event == 'snkVariants':
        print('clicked snkVariants')

    if event == "Event":
        print(window.size)

    if event == sg.WIN_CLOSED:
        print("I am done")
        break