import urllib.request
import webbrowser
from assistant_information import name
def check_internet_connection():
    
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

def open_browser():
    #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.open('chrome.exe')
    
     
def open_browser_and_search():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = str(input(name+": can you tell me the web address to search?\n \nMe: "))
    webbrowser.get(chrome_path).open(url)


