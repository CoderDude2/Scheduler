import webbrowser
import os
from plyer import notification

commands = {
    "open":lambda *args: (os.system(f'open {args[0]}')),
    "open-link":lambda *args: (webbrowser.open(args[0])),
    "notify": lambda *args:(notification.notify(title=args[0], message=args[1], timeout=5)),
    "run": lambda *args: (os.system(args[0]))
}

class Action:
    def __init__(self, command, *args):
        self.command = command
        self.args = args

    # Performs the action based on specific parameters
    def Do(self):
        if(self.command in commands):
            commands[self.command](*self.args)
        else:
            print("Command not found")

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

def deserialize(action):
    return Action(action[0], *action[1])

