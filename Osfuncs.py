import os
import webbrowser
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def AbrenoBrowser():
    # then make a url variable
    url = "https://www.geeksforgeeks.org"

    # then call the default open method described above
    webbrowser.open(url)