import webbrowser
import os

actions = [
    'Open Link "https://www.google.com"',
    'Notfiy "Title" "Message"'
]

def openBrowser(url):
    webbrowser.open(url)

def openFile(path):
    os.system(f'open {path}')

def openFolder(path):
    os.system(f'open {path}')

tokens = []
token = ''

for action in actions:
    for char in action:
        token+=char
        if(token == ' '):
            token = ''
        elif(token == 'Open'):
            tokens.append(token)
            token = ''
        elif(token == 'Link'):
            tokens.append(token)
            token = ''
        elif(token == '"'):
            string = ''

print(tokens)
print(token)