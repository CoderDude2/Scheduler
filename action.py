import webbrowser
import os
from plyer import notification

class Action:
    def __init__(self, command, *args):
        self.command = command
        self.args = args

    # Performs the action based on specific parameters
    def Do(self):
        if(self.command == "Open"):
            if(self.args[0] == "Link"):
                webbrowser.open(self.args[1])
            elif(self.args[0] == "Path"):
                path = self.args[1]
                if(os.name == "nt"):
                    os.system(f'start {path}')
                else:
                    os.system(f'open "{path}"')
        elif(self.command == "Notify"):
            notification.notify(title=self.args[0], message=self.args[1], timeout=5)
        elif(self.command == "Run"):
            os.system(self.args[0])

    def __str__(self):
        msg = f'{self.command}'
        for arg in self.args:
            msg += ' ' + arg
        return msg
    
    def __repr__(self):
        return f'{self.command} {self.args}'

    # Makes it possible to store Action object in json format
    def serialize(self):
        return [self.command, self.args]