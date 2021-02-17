import webbrowser
import os

def openBrowser(url):
    webbrowser.open(url)

def openFile(path):
    os.system(f'open {path}')

def openFolder(path):
    os.system(f'open {path}')

def notify(title, message):
    os.system(f'osascript -e \'display notification "{message}" with title "{title}"\'')

def parseActions(listOfActions):
    for action in listOfActions:
        action = action.split('+')
        if(action[0] == 'Open' and action[1] == 'Link'):
            openBrowser(action[2])
        elif(action[0] == 'Open' and action[1] == 'File'):
            openFile(action[2])
        elif(action[0] == 'Open' and action[1] == 'Folder'):
            openFolder(action[2])
        elif(action[0] == 'Notify'):
            notify(action[1], action[2])