import os
import webbrowser
import  logging
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def AbrenoBrowser():
    # then make a url variable
    url = "https://www.geeksforgeeks.org"

    # then call the default open method described above
    webbrowser.open(url)

logging.basicConfig(filename='log.log', encoding='utf-8',
                    format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

