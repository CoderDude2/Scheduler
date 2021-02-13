import json
import time

class Event:
    def __init__(self, name, date, _time, actions, repeat):
        self.name = name
        self.date = date
        self._time = _time
        self.actions = actions
        self.repeat = repeat

events = []

def displayEvents():
    for event in events:
        print(event)

def newEvent(name, date, _time, actions, repeat):
    event = Event(name, date, _time, actions, repeat)
    events.append(event)

def loadEvents():
    pass

def writeEvents():
    pass

def main():
    newEvent("Period 1", "2/12/2021", "12:00 PM", ['Open https://www.youtube.com'], "Never")
    displayEvents()

try:
    main()
except KeyboardInterrupt:
    exit()