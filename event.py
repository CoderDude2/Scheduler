import json
import time

class Event:
    def __init__(self, name, date, _time, actions, repeat):
        self.name = name
        self.date = date
        self._time = _time
        self.actions = actions
        self.repeat = repeat
        self.isDone = False

def saveEvents(eventList):
    events = []

    for event in eventList:
        formattedEvent = {
            "name":event.name,
            "date":event.date,
            "_time":event._time,
            "actions":event.actions,
            "repeat":event.repeat,
            "isDone":event.isDone
        }
        events.append(formattedEvent)

    with open('events.json', 'w') as file:
        file.write(json.dumps(events, indent=4))

def loadEvents():
    events = []
    with open('events.json', 'r') as file:
        contents = file.read()

    contents = json.loads(contents)
    for event in contents:
        unformattedEvent = Event(event['name'], event['date'], event['_time'], event['actions'], event['repeat'])
        events.append(unformattedEvent)
    return events

def checkTime(event):
    currentTime = time.localtime()
    eventTime = time.strptime(event._time, "%I:%M %p")
    if(currentTime.tm_hour == eventTime.tm_hour and currentTime.tm_min == eventTime.tm_min):
        return True
    return False

def checkDate(event):
    currentDate = time.localtime()
    eventDate = time.strptime(event.date, "%m/%d/%Y")
    if(currentDate.tm_mday == eventDate.tm_mday and currentDate.tm_mon == eventDate.tm_mon and currentDate.tm_year == eventDate.tm_year):
        return True
    return False