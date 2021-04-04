import traceback
import validators
import json
import PySimpleGUI as sg

import scraper as Scraper

layout = [  [sg.Text('URL'), sg.Input(key='-URL-')],
            [sg.Button('Shoe Palace', size=(20,1)), sg.Button('Shop Nice Kicks', size=(20,1))],
            [sg.T(size=(52,1), key='-NAME-')],
            [sg.Multiline(size=(60, 18), key='-OUTPUT-')] ]
            #justification='center',

window = sg.Window("Jill\'s scraper cause Brian won't download the packages",
                   layout,
                   resizable=True,
                   finalize=True,
                   element_justification='c')

window.set_min_size((400,200))

window.bind('<Configure>',"Event")

try:
    while True:
        event, values = window.read()

        if values != None:
            url = values.setdefault('-URL-', None)
            out = {}
        
        if(url != None and validators.url(url) == True):
            try:
                if event == 'Shoe Palace':
                    data = Scraper.scrapeShoePalanceWebsite(url)
                    out = Scraper.spStock(data)
                    print('clicked shoepalace')
                    print(out)

                elif event == 'Shop Nice Kicks':
                    data = Scraper.scrapeShopNiceKicksWebsite(url)
                    out = Scrape.snkVariants(data)
                    print('clicked snk')
                else:
                    window['-OUTPUT-'].update()

                # Need to set to none to escape the if statement
                url = None
                if len(out) == 2:
                    window['-NAME-'].update(out['name'])
                    window['-OUTPUT-'].update(out['info'])

            except json.decoder.JSONDecodeError as e:
                tb = traceback.format_exc()
                sg.popup_error(f'Cannot scrape website',
                                "Please double check the link")

        if event == "Event":
            print(window.size)

        if event == sg.WIN_CLOSED:
            print("I am done")
            break

except Exception as e:
    tb = traceback.format_exc()
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)

window.close()