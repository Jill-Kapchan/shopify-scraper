import traceback
import validators
import json
import PySimpleGUI as sg

import scraper as Scraper

layout = [  [sg.Text('URL'), sg.Input(key='-URL-')],
            [sg.Text('Shoepalace'), sg.Button('spVariants'), sg.Button('spStock') ],
            [sg.Text('ShopNiceKicks'), sg.Button('snkVariants')],
            [sg.Multiline(size=(50, 15), key='-OUTPUT-')] ]

window = sg.Window('Jill\'s scraper',
                   layout,
                   resizable=True,
                   finalize=True)  # this is the chang

window.set_min_size((600,400))

window.bind('<Configure>',"Event")

try:
    while True:
        event, values = window.read()

        if values != None:
            url = values.setdefault('-URL-', None)
            out = values.setdefault('-OUTPUT-', None)
        
        if(url != None and validators.url(url) == True):
            try:
                if event == 'spVariants':
                    data = Scraper.scrapeShoePalanceWebsite(url)
                    out = Scraper.spVariants(data)
                    print('clicked spVariants')
                    print(out)

                elif event == 'spStock':
                    data = Scraper.scrapeShoePalanceWebsite(url)
                    out = Scraper.spStock(data)
                    print('clicked spStock')
                    print(out)

                elif event == 'snkVariants':
                    data = Scraper.scrapeShopNiceKicksWebsite(url)
                    out = Scrape.snkVariants(data)
                    print('clicked snkVariants')

                # Need to set to none to escape the if statement
                url = None
                window['-OUTPUT-'].update('Hi\n', out)

            except json.decoder.JSONDecodeError as e:
                tb = traceback.format_exc()
                sg.popup_error(f'Scraped the wrong website',
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