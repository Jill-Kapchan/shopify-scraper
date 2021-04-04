import sys
import requests
import json
from bs4 import BeautifulSoup, Comment
        
def spStock(data):  
    name = data["title"]   
    variant = data["variants"]

    out = {'name': name}
    info = '| {:^5} | {:^14} | {:8} |'.format("SIZE", "VARIANT ID", "QUANTITY") + "\n"

    for i in range(len(variant)):
        size = variant[i]["options"][1]
        variant_id = variant[i]["id"]
        quantity = abs(variant[i]["inventory_quantity"])
        #out += '------------------------------------------------\n'
        info += '| {:^5} | {:^14} | {:^8} |'.format(size, variant_id, quantity) + "\n"

    out['info'] = info
    print(out)
    return out

def snkVariants(data):
    product = data["product"]
    variant = product["variants"]
    
    name = variant[0]['name'].split('-')
    name = name[0]

    out = {'name': name}
    info = '| {:^9} | {:^14} |'.format("SIZE", "VARIANT ID") + "\n"

    for i in range(len(variant)):
        size = variant[i]["option1"]
        variant_id = variant[i]["id"]
        info += '| {:^9} | {:^14} |'.format(size, variant_id) + "\n"
    
    out['info'] = info
    print(out)
    return out

def scrapeShopNiceKicksWebsite(url):
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    # Shoepalace
    script = soup.find_all(type="application/json")
    script = script[-1]

    # Convert show_data to string
    show_data = str(script)

    # Find last character of opening script tag
    first = show_data.find( '>' )

    # Find first character of closing script tag
    last = show_data.rfind( '<' )

    # Get whatever is between the indeces
    show_data = show_data[first+2:last]
       
    # Loads show_data string into dictionary    
    data = json.loads( show_data )
    return data

def scrapeShoePalanceWebsite(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()
    
    # Shoepalace
    script = soup.find(id="ProductJson--product-template")

    # Convert show_data to string
    show_data = str(script)

    # Find last character of opening script tag
    first = show_data.find( '>' )

    # Find first character of closing script tag
    last = show_data.rfind( '<' )

    # Get whatever is between the indeces
    show_data = show_data[first+1:last]
    #print(show_data)

    # Loads show_data string into dictionary    
    data = json.loads( show_data )
    return data

def main():
    url = ""
    try:
        url = sys.argv[2]
        try:
            if(sys.argv[1] == "--spStock"):
                data = scrapeShoePalanceWebsite(url)
                spStock(data)
            elif(sys.argv[1] == "--snkVariants"):
                data = scrapeShopNiceKicksWebsite(url)
                snkVariants(data)
            else:
                raise IndexError
                
            # Only works for ShoePalace right now
            #scrapeWebsite(url)
            
        except IndexError:
            print("\n\tMissing arguments")
            print("\t\t--spStock url for ShoePalace stock and variants")
            print("\t\t--snkVariants url for ShopNiceKicks variants")
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print("\nDecoding JSON has failed")
            print("Webpage may not be available")

    except IndexError:
        print("Need a URL as the 2nd argument")
        
if __name__== "__main__":
    main()