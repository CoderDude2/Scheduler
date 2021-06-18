import webbrowser
import os
from plyer import notification

def openBrowser(url):
    webbrowser.open(url)

def openPath(path):
    if(os.name == "nt"):
        os.system(f'start {path}')
    else:
        os.system(f'open "{path}"')

def notify(title, message):
    notification.notify(title=title, message=message, timeout=5)

def runCommand(command):
    os.system(command)

def parseActions(listOfActions):
    for action in listOfActions:
        action = action.split('+')
        if(action[0] == 'Open' and action[1] == 'Link'):
            openBrowser(action[2])
        elif(action[0] == 'Open' and action[1] == 'Path'):
            openPath(action[2])
        elif(action[0] == 'Notify'):
            notify(action[1], action[2])
        elif(action[0] == 'Run'):
            runCommand(action[1])




