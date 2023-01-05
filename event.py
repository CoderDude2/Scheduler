import json
import os
import time

import action

class Event:
    def __init__(self, name=None, date=None, _time = None, actions = [], repeat = [], ran=False):
        self.name = name
        self.date = date
        self._time = _time
        self.actions = actions
        self.repeat = repeat
        self.ran = ran
    
    def serialize(self):
        formattedEvent = {
            "name": self.name,
            "date": self.date,
            "_time":self._time,
            "actions": [a.serialize() for a in self.actions],
            "repeat": self.repeat,
            "ran": self.ran
        }
        return formattedEvent

def deserialize(event):
    formatted_actions = [action.deserialize(a) for a in event['actions']]
    unformatted_event = Event(event['name'], event['date'], event['_time'], formatted_actions, event['repeat'], event['ran'])
    return unformatted_event
    

#Converts the Event object into a dictionary and saves it to the events.json file
def saveEvents(eventList):
    events = []

    for event in eventList:
        events.append(event.serialize())

    with open('events.json', 'w+') as file:
        file.write(json.dumps(events, indent=4))

#opens the events.json file and converts the contents into Event objects, the list of objects are then returned
def loadEvents():
    if(os.path.isfile('events.json')):
        events = []
        with open('events.json', 'r') as file:
            contents = file.read()

        contents = json.loads(contents)
        for event in contents:
            deserialized_event = deserialize(event)
            # unformattedEvent = Event(event['name'], event['date'], event['_time'], actions, event['repeat'], event['ran'])

            events.append(deserialized_event)
        return events
    # If events.json file does not exist, create it and initialize it
    return []

#compares the time of the passed in event with the current local time
def checkTime(event):
    try:
        currentTime = time.localtime()
        eventTime = time.strptime(event._time, "%I:%M %p")
        if(currentTime.tm_hour == eventTime.tm_hour and currentTime.tm_min == eventTime.tm_min):
            return True
        return False
    except ValueError:
        print("Incorrect Time Format!")

#compares the date of the passed in event with the current date
def checkDate(event):
    try:
        currentDate = time.localtime()
        eventDate = time.strptime(event.date, "%m/%d/%Y")
        if(currentDate.tm_mday == eventDate.tm_mday and currentDate.tm_mon == eventDate.tm_mon and currentDate.tm_year == eventDate.tm_year):
            return True
        return False
    except ValueError:
        print("Invalid Date Format!")

def checkDay(event):
    currentDay = time.localtime().tm_wday
    for num in event.repeat:
        if(num == currentDay):
            return True    
    return False

def checkDateGTE(event):
    eventDate = time.strptime(event.date, "%m/%d/%Y")
    if(time.localtime() >= eventDate):
        return True
    return False
