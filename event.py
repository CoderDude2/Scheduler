import json
import time

class Event:
    def __init__(self, name, date, _time, actions, repeat, ran=False):
        self.name = name
        self.date = date
        self._time = _time
        self.actions = actions
        self.repeat = repeat
        self.ran = ran

#Converts the Event object into a dictionary and saves it to the events.json file
def saveEvents(eventList):
    events = []

    for event in eventList:
        formattedEvent = {
            "name":event.name,
            "date":event.date,
            "_time":event._time,
            "actions":event.actions,
            "repeat":event.repeat,
            "ran":event.ran
        }
        events.append(formattedEvent)

    with open('events.json', 'w') as file:
        file.write(json.dumps(events, indent=4))

#opens the events.json file and converts the contents into Event objects, the list of objects are then returned
def loadEvents():
    events = []
    with open('events.json', 'r') as file:
        contents = file.read()

    contents = json.loads(contents)
    for event in contents:
        unformattedEvent = Event(event['name'], event['date'], event['_time'], event['actions'], event['repeat'], event['ran'])
        events.append(unformattedEvent)
    return events

#compares the time of the passed in event with the current local time
def checkTime(event):
    currentTime = time.localtime()
    eventTime = time.strptime(event._time, "%I:%M %p")
    if(currentTime.tm_hour == eventTime.tm_hour and currentTime.tm_min == eventTime.tm_min):
        return True
    return False

#compares the date of the passed in event with the current date
def checkDate(event):
    currentDate = time.localtime()
    eventDate = time.strptime(event.date, "%m/%d/%Y")
    if(currentDate.tm_mday == eventDate.tm_mday and currentDate.tm_mon == eventDate.tm_mon and currentDate.tm_year == eventDate.tm_year):
        return True
    return False

def checkDay(event):
    currentDay = time.localtime().tm_wday
    for num in event.repeat:
        if(num == currentDay):
            return True
        else:
            return False

